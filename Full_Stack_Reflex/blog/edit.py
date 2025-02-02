import reflex as rx
from ..ui.base import base_page


class EditExampleState(rx.State):
    title: str = "Hello"
    content: str = "This is blog post"

    def handle_submit(self, form_data):
        print(form_data)

    def handle_content_change(self, value):
        self.content = value

def blog_post_edit_sample() -> rx.Component:
    return rx.form(
            rx.vstack(
                rx.hstack(
                    rx.input(
                        default_value=EditExampleState.title,
                        name="title",
                        placeholder="Title",
                        required=True,
                        type='text',
                        width='100%',
                    ),
                    width='100%'
                ),
                rx.text_area(
                    value=EditExampleState.content,
                    on_change=EditExampleState.handle_content_change,
                    name='content',
                    placeholder="Your message",
                    required=True,
                    height='50vh',
                    width='100%',
                ),
                rx.button("Submit", type="submit"),
            ),
            on_submit=EditExampleState.handle_submit,
            reset_on_submit=False,
    )

def blog_post_edit_page() -> rx.Component:

    my_form = blog_post_edit_sample()

    my_child = rx.vstack(
            rx.heading("Edit Blog Post", size="8"),
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