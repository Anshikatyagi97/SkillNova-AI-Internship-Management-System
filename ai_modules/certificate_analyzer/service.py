"""
AI Certificate Eligibility Analyzer - Service Layer

TODO (Interns):
1. Implement `evaluate_certificate_eligibility()` combining:
   attendance %, task completion %, project submissions,
   mentor feedback rating, and GitHub activity into one decision.
2. Implement `generate_eligibility_explanation()` - natural-language
   justification for the decision.
"""

from typing import Dict


def evaluate_certificate_eligibility(intern_id: str) -> Dict:
    """
    Determine certificate status for an intern: "Eligible",
    "Not Eligible", or "Needs Improvement".

    TODO: Define clear weighted thresholds, e.g.:
          - attendance >= 75% AND completion >= 80% -> Eligible
          - attendance < 50% OR completion < 40% -> Not Eligible
          - everything else -> Needs Improvement
          Pull the real attendance/completion/feedback/github numbers
          from the other AI modules / database instead of hardcoding.
    """
    return {
        "intern_id": intern_id,
        "status": "Needs Improvement",
        "explanation": "TODO: replace with a real AI-generated explanation.",
    }


def generate_eligibility_explanation(metrics: Dict) -> str:
    """
    Given a metrics dict (attendance, completion, feedback, github),
    produce a natural-language explanation for the eligibility decision.

    TODO: Feed `metrics` into an LLM prompt to produce a clear,
          personalized explanation paragraph.
    """
    return "TODO: AI-generated explanation goes here."
