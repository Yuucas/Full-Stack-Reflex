import reflex as rx 
from . import state
from ..utils import get_utc_now
from datetime import datetime, timezone


def blog_post_add_form() -> rx.Component:
    return rx.form(
            rx.vstack(
                rx.hstack(
                    rx.input(
                        name="title",
                        placeholder="Title",
                        required=True,
                        type='text',
                        width='100%',
                    ),
                    width='100%'
                ),
                rx.text_area(
                    name='content',
                    placeholder="Your message",
                    required=True,
                    height='50vh',
                    width='100%',
                ),
                rx.button("Submit", type="submit"),
            ),
            on_submit=state.BlogAddPostFormState.handle_submit,
            reset_on_submit=True,
    )


def blog_post_edit_form() -> rx.Component:

    post = state.BlogEditFormState.post
    title = post.title
    post_content = state.BlogEditFormState.post_content
    # publish_active = post.publish_active

    date = get_utc_now().date()
    time = get_utc_now().strftime("%#H:%M")

    print("Time: ", time)

    return rx.form(
            rx.box(
                rx.input(
                    type='hidden',
                    name='post_id',
                    value=post.id,
            ),
            display='none'
            ),
            rx.vstack(
                rx.hstack(
                    rx.input(
                        default_value=title,
                        name="title",
                        placeholder="Title",
                        required=True,
                        type='text',
                        width='100%',
                    ),
                    width='100%'
                ),
                rx.text_area(
                    value=post_content,
                    on_change=state.BlogEditFormState.set_post_content,
                    name='content',
                    placeholder="Your message",
                    required=True,
                    height='50vh',
                    width='100%',
                ),
                rx.flex(
                    rx.switch(
                        default_checked=state.BlogEditFormState.post_publish_active,
                        on_change=state.BlogEditFormState.set_post_publish_active,
                        name='publish_active'
                    ),
                    rx.text("Publish Active"),
                    spacing='2',
                ),
                rx.cond(
                    state.BlogEditFormState.post_publish_active,
                    rx.box(
                        rx.hstack(
                            rx.input(
                                type='date',
                                default_value=f"{date}",
                                name='publish_date',
                                radius='medium'
                            ),
                            rx.input(
                                type='time',
                                default_value=f"{time}",
                                name='publish_time',
                                radius='medium'
                            ),
                        ),
                        width = '100%'
                    ),
                ),
                rx.button("Submit", type="submit"),
            ),
            on_submit=state.BlogEditFormState.handle_submit,
            reset_on_submit=False,
    )