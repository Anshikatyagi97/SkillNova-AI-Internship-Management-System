"""SQLAlchemy model for storing pre-computed / cached analytics snapshots."""

from sqlalchemy import Column, Integer, String, Float, Date
from backend.database.database import Base


class Analytics(Base):
    """
    Optional table for caching heavy analytics computations
    (e.g. nightly batch jobs) instead of recomputing on every request.

    TODO (Interns):
    - Decide which aggregate metrics are worth caching here
      (e.g. overall_health_score, weekly_completion_rate).
    - Add a `generated_at` timestamp column.
    """

    __tablename__ = "analytics_snapshots"

    snapshot_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    metric_name = Column(String, nullable=False)
    metric_value = Column(Float, nullable=False)
    snapshot_date = Column(Date, nullable=False)
