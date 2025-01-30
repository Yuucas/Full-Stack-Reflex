import reflex as rx
from datetime import datetime
from ..utils import get_utc_now

import sqlalchemy
from sqlmodel import Field

class BlogPostModel(rx.Model, table=True):
    title: str
    content: str
    create_date: datetime = Field(
    default_factory=get_utc_now,
    sa_type=sqlalchemy.DateTime(timezone=True),
    sa_column_kwargs={
        "server_default": sqlalchemy.func.now()
    },
    nullable=True
    )
    update_date: datetime = Field(
    default_factory=get_utc_now,
    sa_type=sqlalchemy.DateTime(timezone=True),
    sa_column_kwargs={
        'onupdate': sqlalchemy.func.now(),
        "server_default": sqlalchemy.func.now()
    },
    nullable=True
    )