"""
Database initialization script.

Run this once to create all tables defined in backend/models/.
Optionally loads the sample CSV datasets from /datasets into the
database so the API has data to serve during development.

Usage:
    python -m backend.database.init_db

TODO (Interns):
- Extend this script to also seed MentorFeedback, Certificate and
  GitHubActivity tables from their respective CSV files.
- Add a `--reset` flag to drop and recreate all tables.
"""

import csv
import os

from backend.database.database import Base, engine, SessionLocal
from backend.models import intern, task, attendance, submission, mentor_feedback, certificate, github_activity, analytics  # noqa: F401
from backend.models.task import Task
from datetime import datetime
from backend.models.attendance import Attendance
from backend.models.submission import Submission
from backend.models.mentor_feedback import MentorFeedback
from backend.models.github_activity import GitHubActivity
from backend.models.certificate import Certificate

DATASETS_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "datasets")


def create_tables():
    """Create all tables in the database if they do not already exist."""
    Base.metadata.create_all(bind=engine)
    print("✅ Tables created successfully.")


def seed_interns():
    """
    Load datasets/interns.csv into the Intern table.

    TODO (Interns):
    - Add error handling for malformed rows.
    - Avoid duplicate inserts if the script is run multiple times.
    """
    from backend.models.intern import Intern

    csv_path = os.path.join(DATASETS_DIR, "interns.csv")
    if not os.path.exists(csv_path):
        print(f"⚠️  {csv_path} not found, skipping intern seeding.")
        return

    db = SessionLocal()
    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            exists = db.query(Intern).filter_by(intern_id=row["intern_id"]).first()
            if exists:
                continue
            intern_obj = Intern(
                intern_id=row["intern_id"],
                name=row["name"],
                email=row["email"],
                domain=row["domain"],
                mentor_name=row["mentor_name"],
                batch=row["batch"],
                start_date=datetime.strptime(row["start_date"], "%Y-%m-%d").date(),
                end_date=datetime.strptime(row["end_date"], "%Y-%m-%d").date(),

                status=row["status"],
            )
            db.add(intern_obj)
        
    db.commit()
    
    db.close()
    print("✅ Interns seeded successfully.")

def seed_tasks():
    """
    Load datasets/tasks.csv into the Task table.
    """

    csv_path = os.path.join(DATASETS_DIR, "tasks.csv")

    if not os.path.exists(csv_path):
        print(f"⚠️ {csv_path} not found, skipping task seeding.")
        return

    db = SessionLocal()

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            exists = db.query(Task).filter_by(task_id=row["task_id"]).first()

            if exists:
                continue

            task = Task(
                task_id=row["task_id"],
                title=row["title"],
                domain=row["domain"],
                week_number=int(row["week_number"]),
                difficulty=row["difficulty"],
            )

            db.add(task)
    
    db.commit()
    
    db.close()

    print("✅ Tasks seeded successfully.")    

def seed_attendance():
    """
    Load datasets/attendance.csv into the Attendance table.
    """

    from datetime import datetime

    csv_path = os.path.join(DATASETS_DIR, "attendance.csv")

    if not os.path.exists(csv_path):
        print(f"⚠️ {csv_path} not found, skipping attendance seeding.")
        return

    db = SessionLocal()

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:

            exists = db.query(Attendance).filter_by(
                attendance_id=int(row["attendance_id"])
            ).first()

            if exists:
                continue

            attendance = Attendance(
                attendance_id=int(row["attendance_id"]),
                intern_id=row["intern_id"],
                date=datetime.strptime(row["date"], "%Y-%m-%d").date(),
                status=row["status"],
            )

            db.add(attendance)

    db.commit()
    db.close()

    print("✅ Attendance seeded successfully.")

def seed_submissions():
    """
    Load datasets/submissions.csv into the Submission table.
    """

    from datetime import datetime

    csv_path = os.path.join(DATASETS_DIR, "submissions.csv")

    if not os.path.exists(csv_path):
        print(f"⚠️ {csv_path} not found, skipping submissions seeding.")
        return

    db = SessionLocal()

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:

            exists = db.query(Submission).filter_by(
                submission_id=int(row["submission_id"])
            ).first()

            if exists:
                continue

            submission = Submission(
                submission_id=int(row["submission_id"]),
                intern_id=row["intern_id"],
                task_id=row["task_id"],
                submission_date=datetime.strptime(
                    row["submission_date"], "%Y-%m-%d"
                ).date(),
                status=row["status"],
                score=float(row["score"]) if row["score"] else None,
            )

            db.add(submission)

    db.commit()
    db.close()

    print("✅ Submissions seeded successfully.")

def seed_mentor_feedback():
    """
    Load datasets/mentor_feedback.csv into the MentorFeedback table.
    """

    csv_path = os.path.join(DATASETS_DIR, "mentor_feedback.csv")

    if not os.path.exists(csv_path):
        print(f"⚠️ {csv_path} not found, skipping mentor feedback seeding.")
        return

    db = SessionLocal()

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:

            exists = db.query(MentorFeedback).filter_by(
                feedback_id=int(row["feedback_id"])
            ).first()

            if exists:
                continue

            feedback = MentorFeedback(
                feedback_id=int(row["feedback_id"]),
                intern_id=row["intern_id"],
                mentor_name=row["mentor_name"],
                week_number=int(row["week_number"]),
                feedback_text=row["feedback_text"],
                rating=int(row["rating"]),
            )

            db.add(feedback)

    db.commit()
    db.close()

    print("✅ Mentor Feedback seeded successfully.")

def seed_github_activity():
    """
    Load datasets/github_activity.csv into the GitHubActivity table.
    """

    from datetime import datetime

    csv_path = os.path.join(DATASETS_DIR, "github_activity.csv")

    if not os.path.exists(csv_path):
        print(f"⚠️ {csv_path} not found, skipping GitHub activity seeding.")
        return

    db = SessionLocal()

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:

            exists = db.query(GitHubActivity).filter_by(
                activity_id=int(row["activity_id"])
            ).first()

            if exists:
                continue

            activity = GitHubActivity(
                activity_id=int(row["activity_id"]),
                intern_id=row["intern_id"],
                repo_name=row["repo_name"],
                commits=int(row["commits"]),
                last_commit_date=datetime.strptime(
                    row["last_commit_date"], "%Y-%m-%d"
                ).date(),
                readme_score=float(row["readme_score"]) if row["readme_score"] else None,
                doc_score=float(row["doc_score"]) if row["doc_score"] else None,
                code_quality_score=float(row["code_quality_score"]) if row["code_quality_score"] else None,
            )

            db.add(activity)

    db.commit()
    db.close()

    print("✅ GitHub Activity seeded successfully.")

def seed_certificates():
    """
    Load datasets/certificates.csv into the Certificate table.
    """

    from datetime import datetime

    csv_path = os.path.join(DATASETS_DIR, "certificates.csv")

    if not os.path.exists(csv_path):
        print(f"⚠️ {csv_path} not found, skipping certificate seeding.")
        return

    db = SessionLocal()

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:

            exists = db.query(Certificate).filter_by(
                certificate_id=int(row["certificate_id"])
            ).first()

            if exists:
                continue

            issue_date = None
            if row["issue_date"]:
                issue_date = datetime.strptime(
                    row["issue_date"], "%Y-%m-%d"
                ).date()

            certificate = Certificate(
                certificate_id=int(row["certificate_id"]),
                intern_id=row["intern_id"],
                status=row["status"],
                issue_date=issue_date,
                remarks=row["remarks"],
            )

            db.add(certificate)

    db.commit()
    db.close()

    print("✅ Certificates seeded successfully.")

if __name__ == "__main__":
    create_tables()
    seed_interns()
    seed_tasks()
    seed_attendance()
    seed_submissions()
    seed_mentor_feedback()
    seed_github_activity()
    seed_certificates()
    # TODO (Interns): call additional seed_* functions for other tables here.
