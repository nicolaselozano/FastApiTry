from sqlalchemy import Table, Column, Integer, String
from app.config.db import meta,engine

users = Table("users", meta, Column(
    "id", Integer, primary_key=True,autoincrement=True),
    Column("name", String(255)),
    Column("email", String(255)),
    Column("password", String(255)))

meta.create_all(engine)
