"""SQLAlchemy model representing an internship Task."""

from sqlalchemy import Column, String, Integer
from backend.database.database import Base


class Task(Base):
    """
    A task/assignment that can be assigned to interns.

    TODO (Interns):
    - Add a `prerequisite_task_id` field to support learning-path sequencing.
    - Add `estimated_hours` for workload estimation.
    """

    __tablename__ = "tasks"

    task_id = Column(String, primary_key=True, index=True)
    title = Column(String, nullable=False)
    domain = Column(String, nullable=False)
    week_number = Column(Integer, nullable=False)
    difficulty = Column(String, default="Beginner")   # Beginner / Intermediate / Advanced
