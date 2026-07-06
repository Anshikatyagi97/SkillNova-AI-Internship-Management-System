"""SQLAlchemy model representing Mentor Feedback given to an intern."""

from sqlalchemy import Column, String, Integer, Text
from backend.database.database import Base


class MentorFeedback(Base):
    """
    Weekly (or ad-hoc) feedback a mentor leaves for an intern.

    TODO (Interns):
    - Add `sentiment_score` (populated by an AI sentiment-analysis step).
    - Add `feedback_date`.
    """

    __tablename__ = "mentor_feedback"

    feedback_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    intern_id = Column(String, nullable=False, index=True)
    mentor_name = Column(String, nullable=False)
    week_number = Column(Integer, nullable=False)
    feedback_text = Column(Text, nullable=False)
    rating = Column(Integer, nullable=False)   # 1-5
