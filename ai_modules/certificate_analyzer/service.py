"""
AI Certificate Eligibility Analyzer - Service Layer
"""

from typing import Dict


def evaluate_certificate_eligibility(intern_id: str) -> Dict:
    """
    Placeholder function.
    """
    return {
        "intern_id": intern_id,
        "status": "Needs Improvement",
        "explanation": "Certificate eligibility will be calculated from real data."
    }


def generate_eligibility_explanation(metrics: Dict) -> str:
    """
    Generate explanation from metrics.
    """

    status = metrics.get("status", "Needs Improvement")

    if status == "Eligible":
        return (
            "The intern has successfully completed all internship "
            "requirements and is eligible for certificate generation."
        )

    if status == "Needs Improvement":
        return (
            "The intern has made good progress but still needs to improve "
            "attendance, task completion or overall performance before "
            "certificate issuance."
        )

    return (
        "The intern is currently not eligible for certification due to "
        "insufficient internship performance."
    )


def get_eligibility_score(status: str) -> int:
    """
    Convert certificate status into a score.
    """

    if status == "Eligible":
        return 100

    if status == "Needs Improvement":
        return 70

    return 40


def get_next_step(status: str) -> str:
    """
    Suggest next action.
    """

    if status == "Eligible":
        return (
            "Congratulations! Your certificate is ready to be issued."
        )

    if status == "Needs Improvement":
        return (
            "Complete pending tasks and improve attendance."
        )

    return (
        "Improve overall internship performance before re-evaluation."
    )