"""SQLAlchemy model representing a Task Submission."""

from sqlalchemy import Column, String, Integer, Date, Float
from backend.database.database import Base


class Submission(Base):
    """
    Record of an intern submitting a task.

    TODO (Interns):
    - Add `file_url` / `repo_url` field for linking actual submitted artifacts.
    - Add `reviewer_comments`.
    """

    __tablename__ = "submissions"

    submission_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    intern_id = Column(String, nullable=False, index=True)
    task_id = Column(String, nullable=False, index=True)
    submission_date = Column(Date, nullable=False)
    status = Column(String, nullable=False)     # on_time / late / pending
    score = Column(Float, nullable=True)         # 0-100, null if not yet graded
