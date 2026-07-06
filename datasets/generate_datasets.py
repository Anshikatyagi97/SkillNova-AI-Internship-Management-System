"""
Generates realistic-looking (fake) sample CSV datasets for local
development and testing of the SkillNova AI Internship Management System.

This script is provided so the starter project ships with usable sample
data. It is NOT part of the AI logic interns need to implement — it is
just a data-generation utility.

Usage:
    python generate_datasets.py

Regenerating will overwrite the existing CSV files in this folder.
"""

import csv
import os
import random
from datetime import date, timedelta

random.seed(42)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DOMAINS = [
    "Backend Development",
    "Frontend Development",
    "AI/ML",
    "Data Science",
    "DevOps",
]

MENTORS = [
    "Ananya Rao",
    "Rohit Sharma",
    "Priya Nair",
    "Karan Mehta",
]

FIRST_NAMES = [
    "Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun", "Sai", "Reyansh", "Krishna",
    "Ishaan", "Rudra", "Ananya", "Diya", "Saanvi", "Myra", "Aadhya", "Kiara",
    "Riya", "Pari", "Anika", "Navya", "Kabir", "Dev", "Yash", "Om", "Aryan",
    "Neha", "Pooja", "Sneha", "Isha", "Tanya",
]
LAST_NAMES = [
    "Sharma", "Verma", "Gupta", "Iyer", "Patel", "Reddy", "Nair", "Singh",
    "Mehta", "Joshi", "Kulkarni", "Rao", "Das", "Kapoor", "Chatterjee",
]

NUM_INTERNS = 35
NUM_TASKS = 35

INTERNSHIP_START = date(2026, 1, 5)


def rand_date(start: date, end: date) -> date:
    delta = (end - start).days
    return start + timedelta(days=random.randint(0, max(delta, 0)))


def generate_interns():
    interns = []
    for i in range(1, NUM_INTERNS + 1):
        intern_id = f"INT-{i:04d}"
        name = f"{random.choice(FIRST_NAMES)} {random.choice(LAST_NAMES)}"
        email = name.lower().replace(" ", ".") + f"{i}@example.com"
        domain = random.choice(DOMAINS)
        mentor_name = random.choice(MENTORS)
        batch = random.choice(["2026-Batch-A", "2026-Batch-B"])
        start_dt = INTERNSHIP_START
        end_dt = start_dt + timedelta(weeks=12)
        status = random.choices(
            ["active", "inactive", "completed"], weights=[0.75, 0.15, 0.10]
        )[0]
        interns.append(
            {
                "intern_id": intern_id,
                "name": name,
                "email": email,
                "domain": domain,
                "mentor_name": mentor_name,
                "batch": batch,
                "start_date": start_dt.isoformat(),
                "end_date": end_dt.isoformat(),
                "status": status,
            }
        )
    return interns


def generate_tasks():
    tasks = []
    task_titles_by_domain = {
        "Backend Development": [
            "Build a REST API with FastAPI", "Implement JWT Authentication",
            "Design a Database Schema", "Write Unit Tests for API Endpoints",
            "Implement Rate Limiting Middleware", "Build a CRUD Service Layer",
        ],
        "Frontend Development": [
            "Build a Responsive Dashboard UI", "Implement Form Validation",
            "Create a Reusable Component Library", "Integrate REST APIs",
            "Build a Data Table with Pagination", "Add Dark Mode Support",
        ],
        "AI/ML": [
            "Train a Text Classification Model", "Build a Recommendation Engine Prototype",
            "Fine-tune a Sentiment Analysis Model", "Build a RAG Pipeline with ChromaDB",
            "Evaluate Model Performance Metrics", "Build a Prompt Engineering Notebook",
        ],
        "Data Science": [
            "Perform Exploratory Data Analysis", "Build a Data Cleaning Pipeline",
            "Create Visualizations with Matplotlib", "Build a Time-Series Forecast",
            "Feature Engineering on Sample Dataset", "Write a Statistical Analysis Report",
        ],
        "DevOps": [
            "Write a Dockerfile for the Backend", "Set Up CI with GitHub Actions",
            "Configure Environment Variables", "Write Deployment Documentation",
            "Set Up Logging and Monitoring", "Automate Testing in a Pipeline",
        ],
    }

    task_counter = 1
    for domain, titles in task_titles_by_domain.items():
        for idx, title in enumerate(titles):
            tasks.append(
                {
                    "task_id": f"TASK-{task_counter:03d}",
                    "title": title,
                    "domain": domain,
                    "week_number": (idx % 6) + 1,
                    "difficulty": random.choice(["Beginner", "Intermediate", "Advanced"]),
                }
            )
            task_counter += 1
    return tasks


def generate_attendance(interns):
    records = []
    attendance_id = 1
    for intern in interns:
        start_dt = date.fromisoformat(intern["start_date"])
        # generate ~30 attendance days per intern (roughly 6 weeks, weekdays only)
        day = start_dt
        days_added = 0
        while days_added < 10:
            if day.weekday() < 5:  # Mon-Fri only
                status = random.choices(
                    ["present", "absent", "late"], weights=[0.80, 0.10, 0.10]
                )[0]
                records.append(
                    {
                        "attendance_id": attendance_id,
                        "intern_id": intern["intern_id"],
                        "date": day.isoformat(),
                        "status": status,
                    }
                )
                attendance_id += 1
                days_added += 1
            day += timedelta(days=1)
    return records


def generate_submissions(interns, tasks):
    records = []
    submission_id = 1
    for intern in interns:
        domain_tasks = [t for t in tasks if t["domain"] == intern["domain"]]
        num_submissions = random.randint(1, min(3, len(domain_tasks)))
        chosen_tasks = random.sample(domain_tasks, k=num_submissions) if domain_tasks else []
        start_dt = date.fromisoformat(intern["start_date"])
        for task in chosen_tasks:
            submission_date = start_dt + timedelta(weeks=task["week_number"], days=random.randint(-2, 4))
            status = random.choices(["on_time", "late", "pending"], weights=[0.65, 0.20, 0.15])[0]
            score = round(random.uniform(50, 100), 1) if status != "pending" else None
            records.append(
                {
                    "submission_id": submission_id,
                    "intern_id": intern["intern_id"],
                    "task_id": task["task_id"],
                    "submission_date": submission_date.isoformat(),
                    "status": status,
                    "score": score if score is not None else "",
                }
            )
            submission_id += 1
    return records


def generate_mentor_feedback(interns):
    records = []
    feedback_id = 1
    sample_feedback = [
        "Good progress this week, keep it up.",
        "Needs to improve consistency in submissions.",
        "Excellent understanding of core concepts.",
        "Struggling with backend fundamentals, needs support.",
        "Great communication during stand-ups.",
        "Should focus more on code documentation.",
        "Consistently meeting deadlines, well done.",
        "Needs to be more proactive in asking questions.",
    ]
    for intern in interns:
        num_feedback = random.randint(1, 3)
        for week in random.sample(range(1, 7), k=num_feedback):
            records.append(
                {
                    "feedback_id": feedback_id,
                    "intern_id": intern["intern_id"],
                    "mentor_name": intern["mentor_name"],
                    "week_number": week,
                    "feedback_text": random.choice(sample_feedback),
                    "rating": random.randint(2, 5),
                }
            )
            feedback_id += 1
    return records


def generate_github_activity(interns):
    records = []
    activity_id = 1
    for intern in interns:
        repo_name = intern["name"].lower().replace(" ", "-") + "-internship-project"
        commits = random.randint(3, 60)
        last_commit = rand_date(date.fromisoformat(intern["start_date"]), date.today())
        records.append(
            {
                "activity_id": activity_id,
                "intern_id": intern["intern_id"],
                "repo_name": repo_name,
                "commits": commits,
                "last_commit_date": last_commit.isoformat(),
                "readme_score": round(random.uniform(2, 10), 1),
                "doc_score": round(random.uniform(2, 10), 1),
                "code_quality_score": round(random.uniform(2, 10), 1),
            }
        )
        activity_id += 1
    return records


def generate_certificates(interns):
    records = []
    cert_id = 1
    for intern in interns:
        status = random.choices(
            ["Eligible", "Not Eligible", "Needs Improvement"], weights=[0.4, 0.2, 0.4]
        )[0]
        issue_date = date.today().isoformat() if status == "Eligible" else ""
        remarks = {
            "Eligible": "All criteria met.",
            "Not Eligible": "Attendance and task completion below threshold.",
            "Needs Improvement": "Close to meeting criteria; needs improvement in one or more areas.",
        }[status]
        records.append(
            {
                "certificate_id": cert_id,
                "intern_id": intern["intern_id"],
                "status": status,
                "issue_date": issue_date,
                "remarks": remarks,
            }
        )
        cert_id += 1
    return records


def write_csv(filename, fieldnames, rows):
    path = os.path.join(BASE_DIR, filename)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"✅ Wrote {len(rows)} rows to {filename}")


def main():
    interns = generate_interns()
    tasks = generate_tasks()
    attendance = generate_attendance(interns)
    submissions = generate_submissions(interns, tasks)
    feedback = generate_mentor_feedback(interns)
    github_activity = generate_github_activity(interns)
    certificates = generate_certificates(interns)

    write_csv(
        "interns.csv",
        ["intern_id", "name", "email", "domain", "mentor_name", "batch", "start_date", "end_date", "status"],
        interns,
    )
    write_csv("tasks.csv", ["task_id", "title", "domain", "week_number", "difficulty"], tasks)
    write_csv("attendance.csv", ["attendance_id", "intern_id", "date", "status"], attendance)
    write_csv(
        "submissions.csv",
        ["submission_id", "intern_id", "task_id", "submission_date", "status", "score"],
        submissions,
    )
    write_csv(
        "mentor_feedback.csv",
        ["feedback_id", "intern_id", "mentor_name", "week_number", "feedback_text", "rating"],
        feedback,
    )
    write_csv(
        "github_activity.csv",
        ["activity_id", "intern_id", "repo_name", "commits", "last_commit_date", "readme_score", "doc_score", "code_quality_score"],
        github_activity,
    )
    write_csv(
        "certificates.csv",
        ["certificate_id", "intern_id", "status", "issue_date", "remarks"],
        certificates,
    )


if __name__ == "__main__":
    main()
