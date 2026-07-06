"""
Backend service layer for the Mentor Dashboard feature.
"""

from ai_modules.mentor_dashboard import service as mentor_ai
from sqlalchemy.orm import Session

from backend.database.database import SessionLocal
from backend.models.intern import Intern
from backend.models.submission import Submission
from backend.models.task import Task

def get_mentor_dashboard(mentor_name: str = None) -> dict:
    """
    Return mentor dashboard statistics using real database data.
    """

    db: Session = SessionLocal()

    try:

        interns_query = db.query(Intern)

        if mentor_name:
            interns_query = interns_query.filter(
                Intern.mentor_name == mentor_name
            )

        interns = interns_query.all()

        total_interns = len(interns)

        active_interns = len(
            [i for i in interns if i.status.lower() == "active"]
        )

        inactive_interns = total_interns - active_interns

        total_tasks = db.query(Task).count()

        total_submissions = db.query(Submission).count()

        late_submissions = (
            db.query(Submission)
            .filter(Submission.status == "late")
            .count()
        )

        average_completion = 0
        performance_data = []


        if total_interns > 0 and total_tasks > 0:

            completion_list = []

            for intern in interns:

                completed = (
                    db.query(Submission)
                    .filter(
                        Submission.intern_id == intern.intern_id
                    )
                    .count()
                )

                completion = (completed / total_tasks) * 100

                completion_list.append(completion)
                performance_data.append(
    {
        "intern_id": intern.intern_id,
        "name": intern.name,
        "completion_percentage": round(completion, 2),
    }
)

            average_completion = round(
                sum(completion_list) / len(completion_list),
                2,
            )
            performance_data.sort(
              key=lambda x: x["completion_percentage"],
              reverse=True,
)

            top_performers = performance_data[:5]

            weak_performers = performance_data[-5:]

        return {

            "mentor_name": mentor_name or "All Mentors",

            "total_interns": total_interns,

            "active_interns": active_interns,

            "inactive_interns": inactive_interns,

            "total_tasks": total_tasks,

            "total_submissions": total_submissions,

            "late_submissions": late_submissions,

            "average_completion_percentage": average_completion,

            "top_performers": top_performers,

            "weak_performers": weak_performers,

            "ai_alerts": [
                "AI alerts will be implemented in the next sprint."
            ],

            "mentor_recommendations": [
                "AI mentor recommendations will be implemented in the next sprint."
            ],
        }

    finally:
        db.close()