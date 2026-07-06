"""Helper utilities for the Analytics Dashboard AI module."""

from collections import Counter
from typing import List, Dict


def count_by_key(records: List[Dict], key: str) -> Dict[str, int]:
    """
    Count occurrences of each distinct value of `key` across a list of
    dict records. Useful for domain distribution / mentor workload.

    TODO (Interns): Use this inside get_domain_distribution() and
    get_mentor_workload() once real records are being queried.
    """
    return dict(Counter(record.get(key) for record in records))
