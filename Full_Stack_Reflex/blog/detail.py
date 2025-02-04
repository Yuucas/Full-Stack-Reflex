import reflex as rx
from .. import navigation
from ..ui.base import base_page
from . import state


def blog_post_detail_page() -> rx.Component:

    edit_button =rx.button(
                    "Edit Post", 
                    on_click=rx.redirect(state.BlogPostState.edit_link_path),
                    color_scheme='indigo',
                    variant='solid'
                    )

    edit_link_check = rx.cond(
        state.BlogPostState.is_editable,
        edit_button,
        edit_button
    )

    my_child = rx.vstack(

        rx.vstack(
            rx.form(
                rx.vstack(
                    rx.heading(state.BlogPostState.post.title, size="8"),
                    rx.divider(),
                    rx.text(
                        state.BlogPostState.post.content,
                        white_space='pre-wrap',
                        size="4",
                        resize='vertical'
                    ),
                    edit_link_check,

                    spacing='7',
                    align='center',

                ),
            ),
        ),
        # rx.heading(state.BlogPostState.post.title, size="8"),


        # rx.text(
        #     state.BlogPostState.post.content,
        #     white_space='pre-wrap',
        #     size="7",
        # ),

        # edit_link_check,
            
        spacing="9",
        justify="between",
        align='center',
        text_align='center',
        wrap='wrap',
        min_height="80vh",
        id='blog-post-detail-page'
    )
    
    return base_page(my_child)