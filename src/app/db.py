import os

from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    DateTime,
)

from sqlalchemy.sql import func

from databases import Database

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
metadata = MetaData()

cards = Table(
    "cards",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("position", Integer),
    Column("title", String(50)),
    Column("type", String(50)),
    Column("created_date", DateTime, default=func.now(), nullable=False)
)

database = Database(DATABASE_URL)
