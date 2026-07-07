"""
AI Attendance & Performance Analyzer - Service Layer

TODO (Interns):
1. Implement attendance percentage calculations (overall/weekly/monthly).
2. Implement `detect_consecutive_absences()`.
3. Implement `predict_attendance_drop()` - flag interns whose attendance
   trend is declining over the last N weeks.
4. Implement `calculate_consistency_score()`.
5. Implement `get_attendance_heatmap_data()` - shape data for a
   calendar-style heatmap on the frontend.
"""

from typing import Dict, List
from backend.ai.llm_service import llm

def get_attendance_percentage(intern_id: str, period: str = "overall") -> float:
    """
    Calculate attendance percentage for an intern.

    period: "overall" | "weekly" | "monthly"

    TODO: Query the Attendance table and compute present_days / total_days * 100.
    """
    return 0.0


def detect_consecutive_absences(intern_id: str) -> int:
    """
    Return the current streak of consecutive absent days for an intern.

    TODO: Walk the Attendance records ordered by date and count the
          trailing streak of "absent" statuses.
    """
    return 0


def predict_attendance_drop(intern_id: str) -> bool:
    """
    Predict whether an intern's attendance is trending downward.

    TODO: Compare attendance % in the last 2 weeks vs. the previous 2 weeks.
          Optionally train a small trend-detection model.
    """
    return False


def calculate_consistency_score(intern_id: str) -> float:
    """
    A single 0-100 score representing how consistent (regular) an
    intern's attendance pattern is (not just the raw percentage).

    TODO: e.g. penalize interns with irregular present/absent patterns
          even if their overall percentage looks acceptable.
    """
    return 0.0


def get_attendance_heatmap_data(intern_id: str) -> List[Dict]:
    """
    Return per-day attendance status shaped for a heatmap visualization.

    TODO: Return a list like:
          [{"date": "2026-01-01", "status": "present"}, ...]
    """
    return []

def generate_ai_attendance_summary(
    intern_id: str,
    attendance_percentage: float,
    late_days: int,
    absent_days: int,
) -> str:
    """
    Generate an AI-powered attendance summary.
    """

    prompt = f"""
You are an AI Internship Mentor.

Intern ID: {intern_id}

Attendance Percentage: {attendance_percentage}%

Late Days: {late_days}

Absent Days: {absent_days}

Write a professional attendance summary in 3-4 sentences.

Include:
- Attendance performance
- Consistency
- Areas of improvement
- Motivation
"""

    return llm.generate_response(prompt)


def predict_attendance_risk(
    attendance_percentage: float,
) -> str:
    """
    Predict attendance risk level.
    """

    if attendance_percentage >= 90:
        return "Low"

    elif attendance_percentage >= 75:
        return "Medium"

    return "High"


def attendance_recommendation(
    attendance_percentage: float,
    late_days: int,
) -> str:
    """
    Generate attendance recommendation.
    """

    if attendance_percentage < 60:
        return (
            "Improve attendance immediately and meet your mentor weekly."
        )

    if late_days >= 3:
        return (
            "Focus on punctuality to improve overall consistency."
        )

    return (
        "Maintain your current attendance performance."
    )