"""SQLAlchemy model representing an intern's GitHub repository activity."""

from sqlalchemy import Column, String, Integer, Date, Float
from backend.database.database import Base


class GitHubActivity(Base):
    """
    Snapshot of a GitHub repository submitted by an intern.

    TODO (Interns):
    - Add `branch_count`, `open_issues`, `pull_requests`.
    - Populate `doc_score` / `code_quality_score` via the github_analyzer module.
    """

    __tablename__ = "github_activity"

    activity_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    intern_id = Column(String, nullable=False, index=True)
    repo_name = Column(String, nullable=False)
    commits = Column(Integer, default=0)
    last_commit_date = Column(Date, nullable=True)
    readme_score = Column(Float, nullable=True)       # 0-10
    doc_score = Column(Float, nullable=True)           # 0-10
    code_quality_score = Column(Float, nullable=True)  # 0-10
