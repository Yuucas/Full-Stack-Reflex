"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""
    label = "Welcome to Reflex!"

    def handle_title_input_change(self, val):
        self.label = val

def navbar() -> rx.Component:
    return rx.heading("SaaS", size="6"),

def base_page(child: rx.Component, hide_navbar=False, *args, **kwargs) -> rx.Component:
    # Print the type of the arguments in the base page
    print([type(x) for x in args])
    # Check if the child is a component
    if not isinstance(child, rx.Component):
        child = rx.heading("This is not a valid child element")
    if hide_navbar:
        return (
            child,
            rx.logo(),
            rx.color_mode.button(position="bottom-left"),
        )
    # Child: is used to call the components of the container in every page
    return rx.container(
        child,
        navbar(),
        rx.logo(),
        rx.color_mode.button(position="bottom-left"),
    )

def index() -> rx.Component:
    return base_page(
        rx.vstack(
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.input(
                default_value=State.label,
                on_change=State.handle_title_input_change,
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        hide_navbar=True
    )


app = rx.App()
app.add_page(index)
