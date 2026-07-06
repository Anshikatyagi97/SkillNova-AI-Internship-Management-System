"""
Backend service layer for the GitHub & Code Review Assistant feature.
"""

from ai_modules.github_analyzer import service as github_ai

from sqlalchemy.orm import Session

from backend.database.database import SessionLocal
from backend.models.github_activity import GitHubActivity

def get_github_analysis(repo_url: str) -> dict:
    """
    Return GitHub repository analysis from database.
    """

    db: Session = SessionLocal()

    try:

        activity = (
            db.query(GitHubActivity)
            .filter(GitHubActivity.repo_name == repo_url)
            .first()
        )

        if not activity:
            return {
                "repo_url": repo_url,
                "message": "Repository not found."
            }

        average_score = round(
            (
                activity.readme_score +
                activity.doc_score +
                activity.code_quality_score
            ) / 3,
            2,
        )

        if average_score >= 8:
            health = "Excellent"

        elif average_score >= 6:
            health = "Good"

        elif average_score >= 4:
            health = "Needs Improvement"

        else:
            health = "Poor"

        suggestions = []

        if activity.readme_score < 7:
            suggestions.append("Improve README documentation.")

        if activity.doc_score < 7:
            suggestions.append("Add more project documentation.")

        if activity.code_quality_score < 7:
            suggestions.append("Refactor code and improve quality.")

        if activity.commits < 10:
            suggestions.append("Increase commit frequency.")

        if not suggestions:
            suggestions.append("Excellent repository. Keep it up!")

        return {

            "repo_name": activity.repo_name,

            "commits": activity.commits,

            "last_commit_date": activity.last_commit_date,

            "readme_score": activity.readme_score,

            "documentation_score": activity.doc_score,

            "code_quality_score": activity.code_quality_score,

            "repository_health": health,

            "overall_score": average_score,

            "ai_feedback": suggestions,
        }

    finally:
        db.close()