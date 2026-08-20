from datetime import datetime
from sqlmodel import Field, SQLModel


class Note(SQLModel, table=True):
    __tablename__ = "note"

    id: int = Field(primary_key=True, index=True)
    title: str | None = Field(unique=True)
    author: str | None
    date_creation: datetime = Field(default_factory=datetime.now)
    date_update: datetime = Field(default_factory=datetime.now)
    type: str | None = Field(default=None)