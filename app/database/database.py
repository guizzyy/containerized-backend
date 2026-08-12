from sqlmodel import create_engine, MetaData, SQLModel, Session
from typing import Annotated
from fastapi import Depends


POSTGRES_DB = "postgresql+psycopg://test_user:Password1.@postgres:5432/web_db"

# Begin the engine connection for the database (it can be multiple connections)
engine = create_engine(
    POSTGRES_DB,
    echo=True                  
)

# Create all the tables and database defined
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Create a session in order to perform database operations
def get_session():
    with Session(engine) as session:
        yield session

session = Annotated[Session, Depends(get_session)]