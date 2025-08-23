# app/database.py
# This file is responsible for the database connection and session management.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# PostgreSQL server connection URL.
# Ensure your PostgreSQL server is running and the credentials are correct.
DATABASE_URL = "postgresql+psycopg2://postgres:chaitu1623@localhost:5432/school_db"

# Create the SQLAlchemy engine. `echo=True` is useful for debugging as it logs SQL queries.
engine = create_engine(DATABASE_URL, echo=True)

# Create a SessionLocal class. Each instance will be a database session.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a Base class for our ORM models to inherit from.
Base = declarative_base()

# Dependency for FastAPI routes to get a database session.
# This ensures the database session is properly opened and closed for each request.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()