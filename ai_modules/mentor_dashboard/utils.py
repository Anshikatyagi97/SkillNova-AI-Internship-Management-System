"""Helper utilities for the Mentor Dashboard AI module."""


def safe_percentage(numerator: int, denominator: int) -> float:
    """Return numerator/denominator*100, guarding against division by zero."""
    if denominator == 0:
        return 0.0
    return round((numerator / denominator) * 100, 2)


# TODO (Interns): Add helpers for ranking/sorting intern lists by
# multiple weighted criteria (completion %, attendance %, feedback rating).
