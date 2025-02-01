from typing import Optional, List
import reflex as rx
from functools import partial

from sqlmodel import select, or_, all_, and_, or_

from .. import navigation
from .model import BlogPostModel

#####################################################################

class BlogPostState(rx.State):
    posts: List[BlogPostModel] = []
    post: Optional[BlogPostModel] = None

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

    def load_posts(self):
        """Load all blog posts."""
        with rx.session() as session:
            result = session.exec(select(BlogPostModel)).all()
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
            except Exception as e:
                print(f"Error fetching post detail: {e}")
                self.post = None

    def get_post(self, post_id):
        pass

    def add_post(self, form_data:dict):
        with rx.session() as session:
            post = BlogPostModel(**form_data)
            # print("adding", post)
            session.add(post)
            session.commit()
            session.refresh(post) # post.id
            # print("added", post)
            self.post = post

#####################################################################

class BlogAddPostFormState(BlogPostState):
    form_data: dict = {}

    def handle_submit(self, form_data):
        self.form_data = form_data
        self.add_post(form_data)

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

