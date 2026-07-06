"""Helper utilities for the Certificate Eligibility Analyzer AI module."""


def weighted_score(metrics: dict, weights: dict) -> float:
    """
    Combine multiple 0-100 metrics into a single weighted score.

    Example:
        weighted_score(
            {"attendance": 80, "completion": 90},
            {"attendance": 0.4, "completion": 0.6}
        )

    TODO (Interns): Tune the weights based on what actually matters
    most for certificate eligibility at SkillNova.
    """
    total = 0.0
    for key, weight in weights.items():
        total += metrics.get(key, 0) * weight
    return round(total, 2)
