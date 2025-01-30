from datetime import datetime, timezone
from typing import List
import asyncio
import reflex as rx

from sqlmodel import select, asc, or_
from .model import ContactEntryModel


class ContactState(rx.State):
    form_data: dict = {}
    entries: List['ContactEntryModel'] = []
    sort_value = ""
    search_value = ""
    did_submit: bool = False

    @rx.var(cache=True)
    def thank_you(self):
        first_name = self.form_data.get('first_name') or " "
        return f"Thank You , {first_name} for submission!"

    async def handle_submit(self, form_data: dict):
        self.form_data = form_data
        data = {}
        # Delete key if it's value is empty
        for key, value in form_data.items():
            if value == "" or value == None:
                continue
            data[key] = value

        # Commit into database
        with rx.session() as session:
            db_entry = ContactEntryModel(
                **form_data
            )
            session.add(db_entry)
            session.commit()
            self.did_submit = True
            yield

        # Sleep the function for 2 seconds
        await asyncio.sleep(2)
        self.did_submit = False
        yield

    @rx.event
    def load_entries(self):
        with rx.session() as session:
            entries = session.exec(
                select(ContactEntryModel)
            ).all()
            self.entries = entries

    @rx.event
    def load_entries_v2(self):
        """Get all users from the database."""
        with rx.session() as session:
            query = select(ContactEntryModel)

            if self.search_value != "":
                search_value = (
                    f"%{self.search_value.lower()}%"
                )
                query = query.where(
                    or_(
                        ContactEntryModel.first_name.ilike(search_value),
                        ContactEntryModel.age.ilike(search_value),
                        ContactEntryModel.email.ilike(search_value),
                        ContactEntryModel.message.ilike(search_value),
                        ContactEntryModel.create_date.ilike(search_value),
                    )
                )

            if self.sort_value != "":
                sort_column = getattr(
                    ContactEntryModel, self.sort_value
                )
                order = asc(sort_column)
                query = query.order_by(order)

            self.entries = session.exec(query).all()

    @rx.event
    def sort_values(self, sort_value):
        self.sort_value = sort_value
        self.load_entries_v2()

    @rx.event
    def filter_values(self, search_value):
        self.search_value = search_value
        self.load_entries_v2()


def show_contacts(contact: ContactEntryModel):
    """Show a customer in a table row."""
    return rx.table.row(
        rx.table.cell(f"{contact.first_name} {contact.last_name}"),
        rx.table.cell(contact.age),
        rx.table.cell(contact.email),
        rx.table.cell(contact.message),
        rx.table.cell(contact.create_date),
    )

def loading_contact_entries_table():
    return rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Full Name"),
                    rx.table.column_header_cell("Age"),
                    rx.table.column_header_cell("Email"),
                    rx.table.column_header_cell("Message"),
                    rx.table.column_header_cell("Submission Date"),
                ),
            ),
            rx.table.body(
                rx.foreach(
                    ContactState.entries, show_contacts
                )
            ),
            on_mount=ContactState.load_entries,
            width="50%",
        )

def loading_contact_entries_table_v2():
    return rx.vstack(
        rx.select.root(
            rx.select.trigger(),
            rx.select.content(
                rx.select.group(
                rx.select.label("Order By:"),
                rx.select.item("Name", value="first_name"),
                rx.select.item("Age", value="age"),
                rx.select.item("E-mail", value="email"),
                rx.select.item("Message", value="message"),
                rx.select.item("Date", value="create_date"),
                ),
            ),
        on_change=lambda value: ContactState.sort_values(
                value
            ),
        ),
        rx.input(
            placeholder="Search here...",
            on_change=lambda value: ContactState.filter_values(
                value
            ),
        ),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Full Name"),
                    rx.table.column_header_cell("Age"),
                    rx.table.column_header_cell("Email"),
                    rx.table.column_header_cell("Message"),
                    rx.table.column_header_cell("Submission Date"),
                ),
            ),
            rx.table.body(
                rx.foreach(
                    ContactState.entries, show_contacts
                )
            ),
            on_mount=ContactState.load_entries_v2,
            width="100%",
        ),
        width="100%",
    )