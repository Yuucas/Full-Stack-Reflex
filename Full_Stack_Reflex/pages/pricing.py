import reflex as rx
from ..ui.base import base_page

def pricing_page() -> rx.Component:

    my_child = rx.vstack(
            rx.heading("Pricing Page", size="9"),
            rx.text(
                "Give me the money bitch",
                size="5",
                color_scheme='gold'
            ),
            spacing="5",
            justify="center",
            align='center',
            text_align='center',
            min_height="85vh",
            id='pricing-child'
        )
    
    return base_page(my_child)