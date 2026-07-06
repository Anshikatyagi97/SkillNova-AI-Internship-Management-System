"""Helper utilities for the Progress Tracker AI module."""

from datetime import date, timedelta


def days_since(target_date: date) -> int:
    """Return number of days between `target_date` and today."""
    return (date.today() - target_date).days


def is_inactive(last_activity_date: date, threshold_days: int = 7) -> bool:
    """
    Simple helper: an intern is considered inactive if their last
    recorded activity is older than `threshold_days`.

    TODO (Interns): Consider combining multiple signals
    (submissions + attendance + logins) rather than a single date.
    """
    return days_since(last_activity_date) > threshold_days
