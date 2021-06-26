import os

from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String
)

from databases import Database

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
metadata = MetaData()

cards = Table(
    "cards",
    metadata,
    Column("position", Integer, primary_key=True),
    Column("title", String(50)),
    Column("type", String(50)),
)

database = Database(DATABASE_URL)
