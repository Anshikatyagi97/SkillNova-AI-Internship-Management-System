"""Shared Pydantic response schemas used across multiple routes."""

from typing import Any, Optional
from pydantic import BaseModel


class APIResponse(BaseModel):
    """
    Standard response envelope returned by every endpoint in this project.

    success: whether the request was processed without errors.
    message: short human-readable description.
    data: the actual payload (dict / list / None).
    """

    success: bool = True
    message: str = "OK"
    data: Optional[Any] = None


class AIInsight(BaseModel):
    """
    Standard shape for an AI-generated insight / recommendation string.

    TODO (Interns):
    - Extend with `confidence_score` once real models are producing insights.
    - Extend with `category` (e.g. "risk", "recommendation", "summary").
    """

    insight: str
    generated_by: str = "placeholder"   # e.g. "gemini-pro", "groq-llama3", "rule-based"
