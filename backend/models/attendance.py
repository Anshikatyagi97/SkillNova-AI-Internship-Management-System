"""SQLAlchemy model representing a daily Attendance record."""

from sqlalchemy import Column, String, Integer, Date
from backend.database.database import Base


class Attendance(Base):
    """
    One row per intern per day.

    TODO (Interns):
    - Add `check_in_time` / `check_out_time` for detailed late tracking.
    - Add a unique constraint on (intern_id, date).
    """

    __tablename__ = "attendance"

    attendance_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    intern_id = Column(String, nullable=False, index=True)
    date = Column(Date, nullable=False)
    status = Column(String, nullable=False)   # present / absent / late
