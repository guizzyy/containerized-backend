from pydantic import BaseSchema
from datetime import date

class Note(BaseSchema):

    title: str
    author: str
    date_creation: date
    date_update: date
    type: str