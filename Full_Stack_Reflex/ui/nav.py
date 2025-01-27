import reflex as rx


def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="5", weight="medium"), href=url, underline="none"
    )

# id: is used to identify spesific names to components in the browser
def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.link(
                        rx.image(
                        src="/mechanicaai.png",
                        width="3.25em",
                        height="auto",
                        border_radius="25%",
                        ),
                        href='/'
                    ),
                    rx.link(
                        rx.heading(
                        "Mechanica AI", size="7", weight="bold"
                        ),
                        href="/",
                        underline="none"
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home", "/#"),
                    navbar_link("About", "/about"),
                    navbar_link("Pricing", "/pricing"),
                    navbar_link("Contact", "/contact"),
                    spacing="5",
                ),
                rx.hstack(
                    rx.button(
                        "Sign Up",
                        size="3",
                        variant="outline",
                    ),
                    rx.button("Log In", size="3"),
                    spacing="4",
                    justify="end",
                ),
                justify="between",
                align_items="center",
                id="main_page_navbar"
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.link(rx.image(
                        src="/mechanicaai.png",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    href='/'),
                    rx.link(
                        rx.heading(
                        "Mechanica AI", size="6", weight="bold"
                    ),
                    href="/",
                    underline="none"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item(rx.link("Home", href="/", underline="none")),
                        rx.menu.item(rx.link("About", href="/about", underline="none")),
                        rx.menu.item(rx.link("Pricing", href="/pricing", underline="none")),
                        rx.menu.item(rx.link("Contact", href="/contact", underline="none")),
                        rx.menu.separator(),
                        rx.menu.item("Log in"),
                        rx.menu.item("Sign up"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )