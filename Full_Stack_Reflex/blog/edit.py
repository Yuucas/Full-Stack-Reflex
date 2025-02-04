import reflex as rx
from ..ui.base import base_page
from .state import BlogEditFormState
from . import forms



def blog_post_edit_page() -> rx.Component:

    my_form = forms.blog_post_edit_form()
    post = BlogEditFormState.post

    my_child = rx.vstack(
            rx.heading(f"Editing of {post.title}", size="8"),
            rx.desktop_only(
                rx.box(
                    my_form,
                    width='50vw'
                )
            ),
            rx.tablet_only(
                rx.box(
                    my_form,
                    width='75vw'
                )
            ),
            rx.mobile_only(
                rx.box(
                    my_form,
                    width='95vw'
                )
            ),
            spacing="5",
            align="center",
            min_height="95vh",
        )
    return base_page(my_child)