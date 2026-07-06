"""
Backend service layer for the Task Recommendation feature.
"""

from ai_modules.task_recommender import service as task_ai

from sqlalchemy.orm import Session

from backend.database.database import SessionLocal
from backend.models.task import Task
from backend.models.submission import Submission
from backend.models.intern import Intern

def get_task_recommendations(intern_id: str) -> dict:
    """
    Return personalized task recommendations based on intern progress.
    """

    db: Session = SessionLocal()

    try:

        # Check if intern exists
        intern = (
            db.query(Intern)
            .filter(Intern.intern_id == intern_id)
            .first()
        )

        if not intern:
            return {
                "intern_id": intern_id,
                "message": "Intern not found."
            }

        # Fetch completed tasks
        completed_submissions = (
            db.query(Submission)
            .filter(Submission.intern_id == intern_id)
            .all()
        )

        completed_task_ids = {
            submission.task_id for submission in completed_submissions
        }

        # Fetch all tasks for intern's domain
        all_tasks = (
            db.query(Task)
            .filter(Task.domain == intern.domain)
            .order_by(Task.week_number)
            .all()
        )

        # Find the first incomplete task
        recommended_task = None

        for task in all_tasks:
            if task.task_id not in completed_task_ids:
                recommended_task = task
                break

        # If all tasks are completed
        if recommended_task is None:
            return {
                "intern_id": intern_id,
                "message": "🎉 Congratulations! All assigned tasks are completed.",
                "completed_tasks": len(completed_task_ids),
                "recommended_task": None
            }

        # Difficulty based priority
        if recommended_task.difficulty.lower() == "beginner":
            priority = "Medium"
            estimated_hours = 3

        elif recommended_task.difficulty.lower() == "intermediate":
            priority = "High"
            estimated_hours = 5

        else:
            priority = "Very High"
            estimated_hours = 8

        # AI-style Recommendation
        recommendation_reason = (
            f"The next recommended task is '{recommended_task.title}' "
            f"because it follows your current learning path in "
            f"{intern.domain}."
        )

        learning_tip = (
            "Complete this task before moving to higher difficulty topics."
        )

        return {

            "intern_id": intern_id,

            "domain": intern.domain,

            "completed_tasks": len(completed_task_ids),

            "recommended_task": recommended_task.title,

            "task_id": recommended_task.task_id,

            "week_number": recommended_task.week_number,

            "difficulty": recommended_task.difficulty,

            "priority": priority,

            "estimated_hours": estimated_hours,

            "learning_tip": learning_tip,

            "ai_recommendation": recommendation_reason,
        }

    finally:
        db.close()
