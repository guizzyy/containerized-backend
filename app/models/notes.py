from datetime import datetime

from sqlmodel import Field, SQLModel


class Note(SQLModel, table=True):
    __tablename__ = "note"

    id: int = Field(primary_key=True, index=True)
    title: str = Field(unique=True)
    author: str
    date_creation: datetime = Field(default_factory=datetime.now)
    type: str | None = Field(default=None)