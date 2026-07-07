"""
AI Internship Progress Tracker - Service Layer

Responsible for turning raw task/submission/attendance data into
progress insights for a single intern or a whole batch.

TODO (Interns):
1. Implement `get_completion_percentage()` using real Task/Submission data.
2. Implement `predict_slow_progress()` - use a simple heuristic first
   (e.g. completion_rate < 50% and week_number > 2), then upgrade to
   a trained classifier (Scikit-learn) if time allows.
3. Implement `detect_inactive_interns()` - e.g. no submissions in last 7 days.
4. Implement `generate_progress_summary()` - call an LLM (Gemini/Groq via
   LangChain) to turn the raw stats into a natural-language paragraph.
5. Implement `suggest_next_tasks()` - recommend the next logical task(s)
   based on completed tasks and domain.
"""

from typing import Dict, List
from backend.ai.llm_service import llm





def get_completion_percentage(intern_id: str) -> float:
    """
    Calculate what percentage of assigned tasks an intern has completed.

    TODO: Query Submission + Task tables and compute:
          completed_tasks / total_assigned_tasks * 100
    """
    # Placeholder dummy value
    return 0.0


def get_progress_summary(intern_id: str) -> Dict:
    """
    Return a structured progress summary for one intern.

    TODO: Replace the dummy dict below with real aggregated data:
          - total tasks, completed tasks, pending tasks, late submissions
          - overall completion percentage
          - daily/weekly progress trend
    """
    return {
        "intern_id": intern_id,
        "total_tasks": 0,
        "completed_tasks": 0,
        "pending_tasks": 0,
        "late_submissions": 0,
        "completion_percentage": 0.0,
        "note": "TODO: replace with real computed values",
    }


def predict_slow_progress(intern_id: str) -> bool:
    """
    Predict whether an intern is progressing slower than expected.

    TODO: Start with a rule-based heuristic, then optionally train a
          Scikit-learn classifier (e.g. Logistic Regression) using
          historical completion-rate data as features.
    """
    return False


def detect_inactive_interns() -> List[str]:
    """
    Return a list of intern_ids who have had no activity
    (no submissions, no attendance) in the last N days.

    TODO: Implement the actual "no activity" query against the database.
    """
    return []

def generate_ai_progress_narrative(
    intern_id: str,
    completion_percentage: float = 0,
    late_submissions: int = 0,
) -> str:
    """
    Generate an AI-powered internship progress summary.
    """

    prompt = f"""
You are an AI Internship Mentor.

Intern ID: {intern_id}

Completion Percentage: {completion_percentage}%

Late Submissions: {late_submissions}

Write a professional progress summary in 3-4 sentences.

Include:
- Overall performance
- Current progress
- Areas of improvement
- Motivation for the intern
"""

    return llm.generate_response(prompt)

def suggest_next_tasks(intern_id: str) -> List[str]:
    """
    Suggest the next task(s) an intern should attempt.

    TODO: Base this on completed tasks + domain + difficulty progression.
    """
    return []

def get_progress_status(completion_percentage: float) -> str:
    """
    Return progress status based on completion percentage.
    """

    if completion_percentage >= 75:
        return "Excellent Progress"
    elif completion_percentage >= 40:
        return "On Track"
    else:
        return "Behind Schedule"


def get_performance(completion_percentage: float) -> str:
    """
    Return overall performance level.
    """

    if completion_percentage >= 85:
        return "Excellent"
    elif completion_percentage >= 60:
        return "Good"
    elif completion_percentage >= 40:
        return "Average"
    else:
        return "Needs Improvement"


def get_risk_level(completion_percentage: float, late_submissions: int) -> str:
    """
    Estimate internship risk level.
    """

    if completion_percentage < 40 or late_submissions >= 3:
        return "High"

    elif completion_percentage < 70 or late_submissions >= 1:
        return "Medium"

    return "Low"


def get_mentor_recommendation(
    completion_percentage: float,
    late_submissions: int,
) -> str:
    """
    Generate a mentor recommendation.
    """

    if completion_percentage < 40:
        return (
            "Schedule a one-to-one mentoring session and assign "
            "foundational practice tasks."
        )

    if late_submissions >= 3:
        return (
            "Discuss time management and closely monitor upcoming deadlines."
        )

    if completion_percentage >= 75:
        return (
            "Continue current progress and introduce more challenging tasks."
        )

    return (
        "Maintain the current pace and review progress weekly."
    )