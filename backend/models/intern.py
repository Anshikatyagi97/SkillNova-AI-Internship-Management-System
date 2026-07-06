"""SQLAlchemy model representing an Intern."""

from sqlalchemy import Column, String, Date
from backend.database.database import Base


class Intern(Base):
    """
    Core intern record.

    TODO (Interns):
    - Add relationships (tasks, attendance, submissions) using
      SQLAlchemy `relationship()` once all models are finalized.
    """

    __tablename__ = "interns"

    intern_id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    domain = Column(String, nullable=False)          # e.g. "Backend Development"
    mentor_name = Column(String, nullable=False)
    batch = Column(String, nullable=False)            # e.g. "2026-Batch-A"
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    status = Column(String, default="active")         # active / inactive / completed
