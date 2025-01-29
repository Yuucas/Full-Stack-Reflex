import reflex as rx

from .. import contact
from .. import navigation
from ..ui.base import base_page


def contact_entry_list_item(contact: contact.ContactEntryModel):
    '''
    A list item for the contact entry list page.
    contact: contact entry model
    page_type: type of page (e.g. 'desktop' or others)

    Return:
        reflex box
    '''
    return rx.box(
        rx.text(contact.first_name, contact.message),
        id='contact_entry_list_item',
        width='40vw',
        padding='1em'
    )


# How to call "for statement" in reflex (EXAMPLE)
# def foreach_callback(text):
#     return rx.box(rx.text(text))


@rx.page(route=navigation.routes.CONTACT_ENTRIES_ROUTE, on_load=contact.ContactState.list_entries)
def contact_entries_list_page() -> rx.Component:

    return base_page(
        rx.vstack(
            rx.heading("Contact Entries Page", size="9"),
            # rx.foreach(["abc", "bcc", "cde"], foreach_callback) # You can call "for statement" in reflex using rx.foreach()
            rx.foreach(contact.ContactState.entries, contact_entry_list_item),
            spacing="5",
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
            ),
            rx.mobile_and_tablet(
                rx.box(
                    contact.contact_form(),
                    id='contact_form_mobile',
                    width='75vw',
                ),
            ),
            spacing="5",
            justify="center",
            align='center',
            text_align='center',
            min_height="85vh",
            id='contact-child'
        )
    
    return base_page(my_child)