import reflex as rx
from .. import navigation
from ..ui.base import base_page


@rx.page(route=navigation.routes.CONTACT_ROUTE)
def contact_page() -> rx.Component:

    my_child = rx.vstack(
            rx.heading("Contact Page", size="9"),
            rx.text(
                "There is a contact list",
                color_scheme='bronze'
            ),
            spacing="5",
            justify="center",
            align='center',
            text_align='center',
            min_height="85vh",
            id='contact-child'
        )
    
    return base_page(my_child)