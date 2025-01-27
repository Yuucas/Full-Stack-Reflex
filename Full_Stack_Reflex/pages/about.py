import reflex as rx
from ..ui.base import base_page

@rx.page(route="/about")
def about_page() -> rx.Component:

    my_child = rx.vstack(
            rx.heading("About Page", size="9"),
            rx.text(
                "Something cool about page",
            ),
            spacing="5",
            justify="center",
            align='center',
            text_align='center',
            min_height="85vh",
            id='about-child'
        )
    
    return base_page(my_child)