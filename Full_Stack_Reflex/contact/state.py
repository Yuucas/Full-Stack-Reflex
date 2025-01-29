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

    def list_entries(self):
        with rx.session() as session:
            entries = session.exec(
                select(ContactEntryModel)
            ).all()
            self.entries = entries