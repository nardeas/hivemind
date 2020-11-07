from datetime import datetime

from sqlalchemy import Integer, Column, String, Float, DateTime, ForeignKey, Table
from sqlalchemy.dialects.postgresql import UUID

from hivemind.runtime import metadata


User = Table('message', metadata,
    Column('id', Integer, primary_key=True),
    Column("score", Float, nullable=False),

    Column('discussion_id', UUID(as_uuid=True), unique=True, nullable=False),
    Column("user_id", Integer, ForeignKey("user.id"), nullable=False),
    Column("created_at", DateTime, default=datetime.utcnow)
)