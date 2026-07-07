"""
AI Mentor Dashboard - Service Layer

Aggregates intern-level data into mentor-facing dashboard statistics
and AI-generated natural-language insights/alerts.

TODO (Interns):
1. Implement `get_dashboard_stats()` with real counts from the database.
2. Implement `get_top_performers()` / `get_weak_performers()`.
3. Implement `generate_ai_alerts()` - e.g.
   "12 interns are falling behind due to missing weekly submissions."
4. Implement `generate_mentor_recommendations()`.
"""

from typing import Dict, List
from backend.ai.llm_service import llm


def get_dashboard_stats(mentor_name: str = None) -> Dict:
    """
    Return summary statistics for a mentor's dashboard.

    TODO: Replace dummy values with real aggregate queries:
          total_interns, active_interns, inactive_interns,
          weekly_submissions, pending_submissions, completion_rate.
    """
    return {
        "total_interns": 0,
        "active_interns": 0,
        "inactive_interns": 0,
        "weekly_submissions": 0,
        "pending_submissions": 0,
        "completion_rate": 0.0,
    }


def get_top_performers(limit: int = 5) -> List[Dict]:
    """
    Return the top N performing interns.

    TODO: Rank interns by completion_percentage, score average,
          attendance and mentor feedback rating.
    """
    return []


def get_weak_performers(limit: int = 5) -> List[Dict]:
    """
    Return the N interns most at risk of falling behind.

    TODO: Inverse of get_top_performers - low completion + poor attendance.
    """
    return []


def generate_ai_alerts() -> List[str]:
    """
    Generate natural-language alerts for the mentor, e.g.:
      "12 interns are falling behind due to missing weekly submissions."
      "Most interns are struggling with Backend Development tasks."

    TODO: Combine rule-based aggregation with an LLM call to phrase
          the alert naturally. Start rule-based, add LLM polishing later.
    """
    return ["TODO: AI-generated alert goes here."]


def generate_mentor_recommendations() -> List[str]:
    """
    Suggest actions the mentor should take this week.

    TODO: e.g. "Schedule a 1:1 with 3 inactive interns in Batch A."
    """
    return ["TODO: AI-generated mentor recommendation goes here."]

def generate_ai_dashboard_summary(
    total_interns: int,
    active_interns: int,
    inactive_interns: int,
    completion_rate: float,
) -> str:
    """
    Generate AI summary for mentor dashboard.
    """

    prompt = f"""
You are an AI Mentor Assistant.

Dashboard Statistics:

Total Interns: {total_interns}
Active Interns: {active_interns}
Inactive Interns: {inactive_interns}
Overall Completion Rate: {completion_rate}%

Generate a professional dashboard summary in 3-4 sentences.

Include:
- Overall batch performance
- Positive observations
- Areas needing attention
- Mentor guidance
"""

    return llm.generate_response(prompt)


def generate_ai_alerts(
    inactive_interns: int,
    pending_submissions: int,
) -> List[str]:
    """
    Generate AI alerts for mentors.
    """

    alerts = []

    if inactive_interns > 0:
        alerts.append(
            f"{inactive_interns} interns are currently inactive."
        )

    if pending_submissions > 0:
        alerts.append(
            f"{pending_submissions} submissions are still pending review."
        )

    return alerts


def generate_mentor_recommendations(
    completion_rate: float,
) -> List[str]:
    """
    Generate mentor recommendations.
    """

    if completion_rate >= 80:
        return [
            "Recognize top performers.",
            "Assign advanced project work.",
        ]

    elif completion_rate >= 60:
        return [
            "Conduct weekly progress reviews.",
            "Support interns facing challenges.",
        ]

    return [
        "Schedule one-to-one mentoring sessions.",
        "Focus on inactive interns first.",
    ]