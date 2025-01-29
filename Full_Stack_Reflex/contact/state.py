from datetime import datetime, timezone
from typing import List
import asyncio
import reflex as rx

from sqlmodel import select
from .model import ContactEntryModel


class ContactState(rx.State):
    form_data: dict = {}
    entries: List['ContactEntryModel'] = []
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
    def list_entries(self):
        with rx.session() as session:
            entries = session.exec(
                select(ContactEntryModel)
            ).all()
            self.entries = entries


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
            on_mount=ContactState.list_entries,
            width="50%",
        )