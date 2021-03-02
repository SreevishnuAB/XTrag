from sqlalchemy import MetaData, Table, Column, String, PrimaryKeyConstraint
from sqlalchemy.dialects.postgresql import UUID

metadata = MetaData()
tag = Table(
  "xtrag_tag",
  metadata,
  Column("id", UUID),
  Column("tag", String),
  PrimaryKeyConstraint("id", "tag")
)