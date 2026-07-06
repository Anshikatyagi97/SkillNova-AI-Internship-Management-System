"""
Thin wrapper around `requests` for calling the FastAPI backend from
the Streamlit frontend.

Set the BACKEND_URL below (or via the BACKEND_URL environment variable)
to point at your running backend, e.g. http://127.0.0.1:8000

TODO (Interns):
- Add proper error handling / user-facing error messages when the
  backend is unreachable.
- Add request timeouts and retries.
"""

import os
import requests

BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")


def get(path: str, params: dict = None):
    """
    GET helper. Returns the parsed JSON response, or None (with a
    Streamlit-friendly placeholder) if the backend is unreachable.
    """
    try:
        response = requests.get(f"{BACKEND_URL}{path}", params=params, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        return None


def post(path: str, json_body: dict = None):
    """POST helper. Returns the parsed JSON response, or None on failure."""
    try:
        response = requests.post(f"{BACKEND_URL}{path}", json=json_body, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException:
        return None
