"""Helper utilities for the Attendance Analyzer AI module."""

from typing import List


def longest_streak(statuses: List[str], target: str = "absent") -> int:
    """
    Given an ordered list of daily attendance statuses, return the
    longest consecutive streak matching `target`.

    TODO (Interns): Use this (or similar logic) inside
    detect_consecutive_absences() in service.py.
    """
    longest = current = 0
    for status in statuses:
        if status == target:
            current += 1
            longest = max(longest, current)
        else:
            current = 0
    return longest
