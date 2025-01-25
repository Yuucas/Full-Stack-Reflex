import reflex as rx

from .nav import navbar

def base_page(child: rx.Component, *args, **kwargs) -> rx.Component:
    # Print the type of the arguments in the base page
    print([type(x) for x in args])
    # Check if the child is a component
    if not isinstance(child, rx.Component):
        child = rx.heading("This is not a valid child element")

    # Child: is used to call the components of the container in every page
    # id: is used to identify spesific names to components in the browser
    # if you change rx.container to rx.fragment the component will not be rendered as a container
    return rx.fragment(
        navbar(),
        rx.box(
            child,
            bg=rx.color("accent", 3),
            padding="1em",
            # position="fixed",
            # top="0px",
            # z_index="5",
            width="100%",
        ),
        rx.logo(),
        rx.color_mode.button(position="bottom-right", id='dark-and-light-mode-btn'),
        id='my-base-container'
    )