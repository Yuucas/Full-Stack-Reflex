"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

from .ui.base import base_page
from . import blog, contact, pages, navigation


class State(rx.State):
    """The app state."""
    label = "Welcome to Reflex!"

    def handle_title_input_change(self, val):
        self.label = val

    def did_click(self):
        print("Hello Did Click")
        return rx.redirect(path=navigation.routes.ABOUT_ROUTE)


def index() -> rx.Component:

    my_child = rx.vstack(
            rx.heading(State.label, size="9"),
            rx.button("About Money", on_click=State.did_click),
            spacing="5",
            justify="center",
            align='center',
            text_align='center',
            min_height="85vh",
            id='my-child'
        )
    
    return base_page(my_child)


app = rx.App()
app.add_page(index)
app.add_page(pages.about_page, 
             route=navigation.routes.ABOUT_ROUTE)


app.add_page(pages.pricing_page, 
             route=navigation.routes.PRICING_ROUTE)

app.add_page(
    pages.blog_post_list_page, 
    route=navigation.routes.BLOG_POST_ROUTE,
    on_load=blog.BlogPostState.load_posts

)

app.add_page(
    blog.blog_post_add_page, 
    route=navigation.routes.BLOG_POST_ADD_ROUTE
)

app.add_page(
    blog.blog_post_detail_page, 
    route="/blog/[blog_id]",
    on_load=blog.BlogPostState.get_post_detail
)

app.add_page(pages.contact_page, 
             route=navigation.routes.CONTACT_ROUTE)

app.add_page(
    pages.contact_entries_list_page, 
    route=navigation.routes.CONTACT_ENTRIES_ROUTE,
    on_load=contact.ContactState.load_entries_v2
)