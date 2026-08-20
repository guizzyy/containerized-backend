from sqlmodel import create_engine, MetaData, SQLModel, Session
from typing import Annotated
from fastapi import Depends
import os

DATABASE_URL = os.environ["DATABASE_URL"]

# Begin the engine connection for the database (it can be multiple connections)
engine = create_engine(
    DATABASE_URL,
    echo=True                  
)

# Create all the tables and database defined (only for developments)
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Create a session in order to perform database operations
def get_session():
    with Session(engine) as session:
        yield session

session = Annotated[Session, Depends(get_session)]