"""SQLAlchemy model representing Certificate eligibility/issuance."""

from sqlalchemy import Column, String, Integer, Date, Text
from backend.database.database import Base


class Certificate(Base):
    """
    Tracks certificate status for an intern.

    TODO (Interns):
    - Populate `status` and `remarks` using the certificate_analyzer AI module
      instead of static/dummy data.
    """

    __tablename__ = "certificates"

    certificate_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    intern_id = Column(String, nullable=False, index=True)
    status = Column(String, nullable=False)     # Eligible / Not Eligible / Needs Improvement
    issue_date = Column(Date, nullable=True)
    remarks = Column(Text, nullable=True)
