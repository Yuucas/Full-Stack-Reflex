from datetime import datetime, timezone
import asyncio
import reflex as rx

import sqlalchemy
from sqlmodel import Field

from ..utils import get_utc_now

class ContactEntryModel(rx.Model, table=True):
    '''
    There is two way to do the string nullable. 
    The first one is --> string: str | None = None
    The second one is --> string: str = Field(nullable=True)
    '''
    # Define scheme
    first_name: str
    last_name: str | None = None
    age: str = Field(nullable=True)
    email: str = Field(nullable=True)
    message: str
    create_date: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            "server_default": sqlalchemy.func.now()
        },
        nullable=True
        )