from sqlalchemy import TIMESTAMP, Column, Integer, MetaData, String, Table

from database import Base, metadata

note = Table(
    "note",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("content", String),
    Column("date", TIMESTAMP),
    Column("type", String)
)
