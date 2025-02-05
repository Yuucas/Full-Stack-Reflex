from typing import Optional, List
from datetime import datetime
import reflex as rx
from functools import partial

from sqlmodel import select, or_, all_, and_, or_

from .. import navigation
from .model import BlogPostModel
from ..utils import get_utc_now

#####################################################################

class BlogPostState(rx.State):
    posts: List[BlogPostModel] = []
    post: Optional[BlogPostModel] = None
    post_content: str | None = None
    post_publish_active: bool = False

    @rx.var(cache=True)
    def is_editable(self) -> bool:
        return True

    @rx.var(cache=True)
    def edit_link_path(self) -> str:
        return f"{navigation.routes.BLOG_POST_ROUTE}/{self.blog_post_id}/edit" if self.is_editable else f"{navigation.routes.BLOG_POST_ROUTE}/{self.blog_post_id}"
    
    def blog_link_redirect(self):
        if not self.post:
            return rx.redirect(navigation.routes.BLOG_POST_ROUTE)
        return rx.redirect(f"{navigation.routes.BLOG_POST_ROUTE}/{self.post.id}")
    

    def get_id_value(self, id_param) -> Optional[int]:
        """Extract the actual ID value from various possible types."""
        try:
            # Handle partial function case
            if isinstance(id_param, partial):
                # Call the partial function to get the actual value
                actual_value = id_param()
                if isinstance(actual_value, str) and actual_value.isdigit():
                    return int(actual_value)
                return None
            # Handle string case
            elif isinstance(id_param, str) and id_param.isdigit():
                return int(id_param)
            # Handle integer case
            elif isinstance(id_param, int):
                return id_param
            return None
        except Exception as e:
            print(f"Error extracting ID: {e}")
            return None

    @rx.var(cache=True)
    def blog_post_id(self):
        """Get the blog post ID from the URL parameters."""
        return self.router.page.params.get("blog_id", "")

    def load_posts(self, published_only: bool = False):
        """
        Load all blog posts.
        BlogPostModel.publish_active == True --> is used to get the posts that are published date is not None
        BlogPostModel.publish_date < datetime.now() --> is used to get the posts that are published date is not None and is less than the current
        """
        lookup_args = ()
        if published_only:
            lookup_args = (
                (BlogPostModel.publish_active == True) &
                (BlogPostModel.publish_date < get_utc_now())
            )
        with rx.session() as session:
            result = session.exec(select(BlogPostModel).where(
                *lookup_args
                )
            ).all()
            self.posts = result

    def get_post_detail(self):
        """Get details for a specific blog post."""
        with rx.session() as session:
            # Get and process the ID
            post_id = self.get_id_value(self.blog_post_id)
            print("Processed post ID:", post_id)
            
            if post_id is None:
                self.post = None
                return
            
            try:
                result = session.exec(
                    select(BlogPostModel).where(
                        BlogPostModel.id == post_id
                    )
                ).one_or_none()

                self.post = result
                self.post_content = self.post.content
                self.post_publish_active = self.post.publish_active

            except Exception as e:
                print(f"Error fetching post detail: {e}")
                self.post = None

    def get_post(self):
        with rx.session() as session:
            result = session.exec(
                select(BlogPostModel)
            )
            self.posts = result

    def add_post(self, form_data:dict):
        with rx.session() as session:
            post = BlogPostModel(**form_data)
            # print("adding", post)
            session.add(post)
            session.commit()
            session.refresh(post) # post.id
            # print("added", post)
            self.post = post

    def save_post_edits(self, post_id:int, updated_data:dict):
        with rx.session() as session:
            post = session.exec(
                    select(BlogPostModel).where(
                        BlogPostModel.id == post_id
                    )
                ).one_or_none()
            
            if post is None:
                return
            
            for key, value in updated_data.items():
                setattr(post, key, value)

            session.add(post)
            session.commit()
            session.refresh(post)


#####################################################################

class BlogAddPostFormState(BlogPostState):
    form_data: dict = {}

    def handle_submit(self, form_data):

        self.form_data = form_data
        self.add_post(form_data)

        return self.blog_link_redirect()
    
#####################################################################

class BlogEditFormState(BlogPostState):
    form_data: dict = {}
    # post_content: str = ""

    @rx.var(cache=True)
    def publish_display_date(self):
        date = get_utc_now().date()
        if not self.post:
            return date
        if not self.post.publish_date:
            return date
        return date
    
    @rx.var(cache=True)
    def publish_display_time(self):
        time = get_utc_now().strftime("%H:%M:%S")
        if not self.post:
            return time
        if not self.post.publish_date:
            return time
        return time


    def handle_submit(self, form_data):

        self.form_data = form_data
        post_id = form_data.pop('post_id')
        
        # Initialize for the first time
        publish_date, publish_time = None, None
        if 'publish_date' in form_data:
            publish_date = form_data.pop('publish_date')
        if 'publish_time' in form_data:
            publish_time = form_data.pop('publish_time')

        try:
            final_publish_date = datetime.strptime(f"{publish_date} {publish_time}", 
                                                   "%Y-%m-%d %H:%M:%S")
        except:
            final_publish_date = None

        # Check publish active
        publish_active = False
        if 'publish_active' in form_data:
            publish_active = form_data.pop('publish_active') == "on"

        updated_data = {**form_data}
        updated_data['publish_active'] = publish_active
        updated_data['publish_date'] = final_publish_date
        self.save_post_edits(post_id, updated_data)

        return self.blog_link_redirect()


#####################################################################

def blog_post_detail_link(child: rx.Component, post: BlogPostModel):
    """Create a link to a blog post detail page."""

    if post is None:
        return rx.fragment(child)
    post_id = post.id
    root_path = navigation.routes.BLOG_POST_ROUTE
    post_detail_url = f"{root_path}/{post_id}"

    return rx.link(child, href=post_detail_url)

def blog_post_list_item(post: BlogPostModel):

    return rx.box(
        blog_post_detail_link(
            rx.heading(post.title),
            post,
            ),
        padding="1em",
    )

