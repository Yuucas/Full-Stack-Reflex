import reflex as rx

from .. import blog
from .. import navigation
from ..ui.base import base_page



# @rx.page(route=navigation.routes.BLOG_POST_ROUTE, on_load=blog.BlogPostState.load_posts)
def blog_post_list_page() -> rx.Component:

    return base_page(
        rx.vstack(
            rx.heading("Blog Post", size="9"),
            rx.link(
                rx.button("New Post"), 
                href=navigation.routes.BLOG_POST_ADD_ROUTE
                ),
            rx.foreach(blog.BlogPostState.posts, blog.blog_post_list_item),
            spacing="8",
            justify="center",
            align="center",
            min_height="85vh"
        )
    )