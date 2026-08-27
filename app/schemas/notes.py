from datetime import datetime

from pydantic import BaseModel


class GenericResponse(BaseModel):
    message: str

class ResponseNote(BaseModel):

    id: int
    title: str
    author: str
    date_creation: datetime
    type: str | None

class CreateNote(BaseModel):

    title: str
    author: str
    type: str | None