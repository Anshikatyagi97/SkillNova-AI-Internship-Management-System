"""
Backend service layer for the GitHub & Code Review Assistant feature.
"""

from sqlalchemy.orm import Session

from ai_modules.github_analyzer import service as github_ai
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

        overall_score = round(
            (
                activity.readme_score +
                activity.doc_score +
                activity.code_quality_score
            ) / 3,
            2,
        )

        repository_health = github_ai.calculate_repository_health(
            activity.readme_score,
            activity.code_quality_score,
        )

        ai_summary = github_ai.generate_ai_repository_summary(
           repo_url=activity.repo_name,
           commits=activity.commits,
           branches=1,
           readme_score=activity.readme_score,
           code_quality_score=activity.code_quality_score,
)

        recommendations = github_ai.generate_repository_recommendations(
            activity.readme_score,
            activity.code_quality_score,
        )

        return {

            "repo_name": activity.repo_name,

            "commits": activity.commits,

            "branches": 1,

            "last_commit_date": activity.last_commit_date,

            "readme_score": activity.readme_score,

            "documentation_score": activity.doc_score,

            "code_quality_score": activity.code_quality_score,

            "repository_health": repository_health,

            "overall_score": overall_score,

            "ai_summary": ai_summary,

            "recommendations": recommendations,
        }

    finally:
        db.close()