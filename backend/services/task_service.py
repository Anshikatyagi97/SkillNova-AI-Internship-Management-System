"""
Backend service layer for the Task Recommendation feature.
"""

from sqlalchemy.orm import Session

from ai_modules.task_recommender import service as task_ai
from backend.database.database import SessionLocal
from backend.models.intern import Intern
from backend.models.submission import Submission
from backend.models.task import Task


def get_task_recommendations(intern_id: str) -> dict:
    """
    Return personalized task recommendations based on intern progress.
    """

    db: Session = SessionLocal()

    try:

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

        completed_submissions = (
            db.query(Submission)
            .filter(Submission.intern_id == intern_id)
            .all()
        )

        completed_task_ids = {
            submission.task_id
            for submission in completed_submissions
        }

        all_tasks = (
            db.query(Task)
            .filter(Task.domain == intern.domain)
            .order_by(Task.week_number)
            .all()
        )

        recommended_task = None

        for task in all_tasks:
            if task.task_id not in completed_task_ids:
                recommended_task = task
                break

        if recommended_task is None:
            return {
                "intern_id": intern_id,
                "message": "🎉 Congratulations! All assigned tasks are completed.",
                "completed_tasks": len(completed_task_ids),
                "recommended_task": None,
            }

        if recommended_task.difficulty.lower() == "beginner":
            priority = "Medium"
            estimated_hours = 3

        elif recommended_task.difficulty.lower() == "intermediate":
            priority = "High"
            estimated_hours = 5

        else:
            priority = "Very High"
            estimated_hours = 8

        # Demo weak skills (later these can come from identify_weak_skills())
        weak_skills = [
            "Python",
            "FastAPI",
        ]

        ai_summary = task_ai.generate_ai_task_recommendations(
            intern_id=intern_id,
            weak_skills=weak_skills,
        )

        recommended_courses = task_ai.recommend_courses(
            weak_skills
        )

        recommended_projects = task_ai.recommend_projects(
            weak_skills
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

            "weak_skills": weak_skills,

            "recommended_courses": recommended_courses,

            "recommended_projects": recommended_projects,

            "learning_tip": (
                "Complete this task before moving to higher difficulty topics."
            ),

            "ai_summary": ai_summary,
        }

    finally:
        db.close()