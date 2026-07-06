"""
Backend service layer for the Internship Analytics Dashboard feature.
"""

from ai_modules.analytics_dashboard import service as analytics_ai

from sqlalchemy.orm import Session
from sqlalchemy import func

from backend.database.database import SessionLocal
from backend.models.intern import Intern
from backend.models.attendance import Attendance
from backend.models.certificate import Certificate
from backend.models.submission import Submission
from backend.models.github_activity import GitHubActivity

def get_platform_analytics() -> dict:
    """
    Return platform-wide analytics using real database data.
    """

    db: Session = SessionLocal()

    try:

        total_interns = db.query(Intern).count()

        active_interns = (
            db.query(Intern)
            .filter(Intern.status == "active")
            .count()
        )

        inactive_interns = total_interns - active_interns

        total_submissions = db.query(Submission).count()

        eligible_certificates = (
            db.query(Certificate)
            .filter(Certificate.status == "Eligible")
            .count()
        )

        pending_certificates = (
            db.query(Certificate)
            .filter(Certificate.status != "Eligible")
            .count()
        )

        average_readme = db.query(
            func.avg(GitHubActivity.readme_score)
        ).scalar() or 0

        average_doc = db.query(
            func.avg(GitHubActivity.doc_score)
        ).scalar() or 0

        average_code = db.query(
            func.avg(GitHubActivity.code_quality_score)
        ).scalar() or 0

        github_health = round(
            (average_readme + average_doc + average_code) / 3,
            2,
        )

        attendance_records = db.query(Attendance).all()

        total_days = len(attendance_records)

        present_days = len(
            [
                a for a in attendance_records
                if a.status.lower() in ["present", "late"]
            ]
        )

        average_attendance = (
            round((present_days / total_days) * 100, 2)
            if total_days > 0
            else 0
        )

        overall_health = round(
            (
                average_attendance +
                github_health
            ) / 2,
            2,
        )

        if overall_health >= 85:
            health_status = "Excellent"

        elif overall_health >= 70:
            health_status = "Good"

        elif overall_health >= 50:
            health_status = "Average"

        else:
            health_status = "Needs Improvement"

        return {

            "total_interns": total_interns,

            "active_interns": active_interns,

            "inactive_interns": inactive_interns,

            "total_submissions": total_submissions,

            "eligible_certificates": eligible_certificates,

            "pending_certificates": pending_certificates,

            "average_attendance_percentage": average_attendance,

            "github_health_score": github_health,

            "overall_health_score": overall_health,

            "system_status": health_status,

            "ai_summary": (
                f"The internship platform currently has "
                f"{total_interns} interns with an overall "
                f"health score of {overall_health}%."
            ),
        }

    finally:
        db.close()