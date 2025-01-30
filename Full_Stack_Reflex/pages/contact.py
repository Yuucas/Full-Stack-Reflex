import reflex as rx

from .. import contact
from .. import navigation
from ..ui.base import base_page



@rx.page(route=navigation.routes.CONTACT_ENTRIES_ROUTE, on_load=contact.ContactState.load_entries_v2)
def contact_entries_list_page() -> rx.Component:

    return base_page(
        rx.vstack(
            rx.heading("Contact Entries Page", size="9"),
            # rx.foreach(["abc", "bcc", "cde"], foreach_callback) # You can call "for statement" in reflex using rx.foreach()
            contact.loading_contact_entries_table_v2(),
            spacing="8",
            justify="center",
            align="center",
            min_height="85vh"
        )
    )


@rx.page(route=navigation.routes.CONTACT_ROUTE)
def contact_page() -> rx.Component:

    my_child = rx.vstack(
            rx.heading("Contact Page", size="9"),
            rx.cond(condition=contact.ContactState.did_submit, c1=contact.ContactState.thank_you, c2=" "),    
            rx.desktop_only(
                rx.box(
                    contact.contact_form(),
                    id='contact_form_desktop',
                    width='40vw',
                ),
                rx.box(rx.button("Show Contact List"), 
                       size="2", 
                       color_scheme="indigo", 
                       radius="large", 
                       variant="surface", 
                       on_click=rx.redirect(navigation.routes.CONTACT_ENTRIES_ROUTE)),
            ),
            rx.mobile_and_tablet(
                rx.box(
                    contact.contact_form(),
                    id='contact_form_mobile',
                    width='75vw',
                ),
                rx.box(rx.button("Show Contact List"), 
                       size="2", 
                       color_scheme="indigo", 
                       radius="large", 
                       variant="surface", 
                       on_click=rx.redirect(navigation.routes.CONTACT_ENTRIES_ROUTE)),
            ),
            spacing="9",
            justify="center",
            align='center',
            text_align='center',
            min_height="82vh",
            id='contact-child',
        )
    
    return base_page(my_child)