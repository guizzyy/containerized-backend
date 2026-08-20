from collections.abc import Sequence
from contextlib import asynccontextmanager
from typing import Annotated

from database.database import create_db_and_tables, session
from fastapi import FastAPI, HTTPException, Query
from models.notes import Note
from schemas.notes import CreateNote, ResponseNote
from sqlmodel import select


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(
    lifespan=lifespan
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
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    return note

@app.post("/notes", response_model=ResponseNote)
def create_note(
    db: session,
    note: CreateNote
):
    db_note = Note(**note.model_dump())
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note


