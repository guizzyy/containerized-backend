from pydantic import BaseModel
from datetime import date

class ResponseNote(BaseModel):

    id: int
    title: str
    author: str
    date_creation: date
    date_update: date
    type: str

class CreateNote(BaseModel):

    title: str
    author: str
    type: str