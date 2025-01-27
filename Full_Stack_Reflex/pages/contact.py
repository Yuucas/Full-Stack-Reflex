import reflex as rx
from .. import navigation
from ..ui.base import base_page


class ContactState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        print(form_data)
        self.form_data = form_data

@rx.page(route=navigation.routes.CONTACT_ROUTE)
def contact_page() -> rx.Component:
    contact_form = rx.form(
                rx.vstack(
                        rx.input(
                            name="first_name",
                            placeholder="First Name",
                            type='text',
                            required=True,
                        ),
                        rx.input(
                            name="last_name",
                            placeholder="Last Name",
                            type='text',
                        ),
                        rx.input(
                            name="email",
                            placeholder="Email",
                            type='email',
                            required=True,
                        ),
                        rx.text_area(
                            name='messgae',
                            placeholder='Message',
                            type='text',
                            required=True,
                        ),
                        rx.button("Submit", type="submit"),
                        align='center',
                    ),
                    on_submit=ContactState.handle_submit,
                    reset_on_submit=True,
            ),
    my_child = rx.vstack(
            rx.heading("Contact Page", size="9"),
            contact_form,
            spacing="7",
            justify="center",
            align='center',
            text_align='center',
            min_height="85vh",
            id='contact-child'
        )
    
    return base_page(my_child)