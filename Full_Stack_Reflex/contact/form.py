import reflex as rx
from .. import contact


def contact_form() -> rx.Component:
    return  rx.form(
                rx.vstack(
                    rx.hstack(
                        rx.input(
                            name="first_name",
                            placeholder="First Name",
                            type='text',
                            required=True,
                            width='100%'
                        ),
                        rx.input(
                            name="last_name",
                            placeholder="Last Name",
                            type='text',
                            width='100%'
                        ),
                        rx.input(
                            name="age",
                            placeholder="Age",
                            type='text',
                            width='100%'
                        ),
                        width='100%',
                        align='stretch'
                    ),
                    rx.input(
                        name="email",
                        placeholder="Email",
                        type='email',
                        required=True,
                        width='100%'
                    ),
                    rx.text_area(
                        name='message',
                        placeholder='Message',
                        type='text',
                        required=True,
                        width='100%',
                        height='16vh'
                    ),
                    rx.button("Submit", type="submit"),
                # align='center',
                ),
                on_submit=contact.ContactState.handle_submit,
                reset_on_submit=True,
            )

    