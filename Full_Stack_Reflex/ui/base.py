import reflex as rx

from .nav import navbar

def base_page(child: rx.Component, *args, **kwargs) -> rx.Component:
    # Print the type of the arguments in the base page
    print([type(x) for x in args])
    # Check if the child is a component
    if not isinstance(child, rx.Component):
        child = rx.heading("This is not a valid child element")

    # Child: is used to call the components of the container in every page
    return rx.container(
        navbar(),
        child,
        # rx.logo(),
        rx.color_mode.button(position="top-right"),
    )