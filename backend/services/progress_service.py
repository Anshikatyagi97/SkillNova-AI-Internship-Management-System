"""
Backend service layer for the Progress Tracker feature.

Bridges the API routes and the ai_modules/progress_tracker AI logic.
Currently returns dummy/placeholder data so the API is runnable
before the AI logic is implemented.
"""

from ai_modules.progress_tracker import service as progress_ai
from sqlalchemy.orm import Session

from backend.database.database import SessionLocal
from backend.models.intern import Intern
from backend.models.task import Task
from backend.models.submission import Submission

def get_intern_progress(intern_id: str) -> dict:
    """
    Return progress data for a single intern using real database data.
    """

    db: Session = SessionLocal()

    try:
        intern = db.query(Intern).filter(
            Intern.intern_id == intern_id
        ).first()

        if not intern:
            return {
                "error": f"Intern '{intern_id}' not found."
            }

        total_tasks = db.query(Task).count()

        completed_tasks = (
            db.query(Submission)
            .filter(Submission.intern_id == intern_id)
            .count()
        )

        late_submissions = (
            db.query(Submission)
            .filter(
                Submission.intern_id == intern_id,
                Submission.status == "late"
            )
            .count()
        )

        pending_tasks = max(total_tasks - completed_tasks, 0)

        completion_percentage = (
            (completed_tasks / total_tasks) * 100
            if total_tasks > 0
            else 0
        )

        return {
            "intern_id": intern.intern_id,
            "name": intern.name,
            "domain": intern.domain,
            "mentor": intern.mentor_name,
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "pending_tasks": pending_tasks,
            "late_submissions": late_submissions,
            "completion_percentage": round(completion_percentage, 2),
            "progress_status": progress_ai.get_progress_status(
    completion_percentage
),

"performance": progress_ai.get_performance(
    completion_percentage
),

"risk_level": progress_ai.get_risk_level(
    completion_percentage,
    late_submissions,
),

"mentor_recommendation": progress_ai.get_mentor_recommendation(
    completion_percentage,
    late_submissions,
),

"is_slow_progress": progress_ai.predict_slow_progress(intern_id),

"ai_summary": progress_ai.generate_ai_progress_narrative(
    intern_id=intern_id,
    completion_percentage=round(completion_percentage, 2),
    late_submissions=late_submissions,
),


"suggested_next_tasks": progress_ai.suggest_next_tasks(
    intern_id
),
        }

    finally:
        db.close()

def get_inactive_interns() -> list:
    """Return the list of currently inactive interns (dummy data for now)."""
    # TODO (Interns): Wire this to progress_ai.detect_inactive_interns()
    return ["INT-0007", "INT-0021"]
