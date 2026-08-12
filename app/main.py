from fastapi import FastAPI, Query
from schemas.notes import ResponseNote, CreateNote
from database.database import session
from typing import Sequence, Annotated
from sqlmodel import select
from models.notes import Note

app = FastAPI(
    openapi_prefix="/app"
)


@app.get("/notes", response_model=Sequence[ResponseNote])
def get_full_notes(
    db: session,
    offset: int | None = 0,
    limit: Annotated[int, Query(le=100)] = 100
):
    notes = db.exec(select(Note).offset(offset).limit(limit)).all()
    return notes


@app.get("/notes/{id}", response_model=ResponseNote)
def get_note_by_id(
    db: session,
    id: int
):
    note = db.exec(select(Note).where(Note.id == id)).one_or_none()
    return note

@app.post("/notes", response_model=ResponseNote)
def create_note(
    db: session,
    note: CreateNote
):
    db.add(note)
    db.commit()
    db.refresh(note)
    return note
