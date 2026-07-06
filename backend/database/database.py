"""
Database connection and session management (SQLAlchemy).

This module creates the SQLAlchemy engine, session factory, and the
declarative Base class that all ORM models inherit from.

TODO (Interns):
- Add connection pooling configuration for production (e.g. Postgres).
- Add async engine support if you migrate to async SQLAlchemy.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from backend.config.settings import settings

# `check_same_thread` is only needed for SQLite
connect_args = {"check_same_thread": False} if settings.DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(settings.DATABASE_URL, connect_args=connect_args, echo=False)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """
    FastAPI dependency that yields a database session and
    guarantees it is closed after the request finishes.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
