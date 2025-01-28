import reflex as rx
from .. import navigation
from ..ui.base import base_page


class ContactState(rx.State):
    form_data: dict = {}
    did_submit: bool = False

    @rx.var(cache=True)
    def thank_you(self):
        first_name = self.form_data.get('first_name')
        return f"Thank You , {first_name} for submission!" if first_name else "Submission if failed!"

    def handle_submit(self, form_data: dict):
        print(form_data)
        self.form_data = form_data
        self.did_submit = True

@rx.page(route=navigation.routes.CONTACT_ROUTE)
def contact_page() -> rx.Component:
    contact_form = rx.form(
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
                    on_submit=ContactState.handle_submit,
                    reset_on_submit=True,
            ),
    my_child = rx.vstack(
            rx.heading("Contact Page", size="9"),
            rx.cond(condition=ContactState.did_submit, c1=ContactState.thank_you, c2=" "),    
            rx.desktop_only(
                rx.box(
                    contact_form,
                    id='contact_form_desktop',
                    width='40vw',
                )   
            ),
            rx.mobile_and_tablet(
                rx.box(
                    contact_form,
                    id='contact_form_mobile',
                    width='75vw',
                )
            ),
            spacing="5",
            justify="center",
            align='center',
            text_align='center',
            min_height="85vh",
            id='contact-child'
        )
    
    return base_page(my_child)