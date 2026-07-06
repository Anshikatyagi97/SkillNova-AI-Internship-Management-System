"""API routes for Module 2 — AI Mentor Dashboard."""

from fastapi import APIRouter
from typing import Optional
from backend.api.schemas.common import APIResponse
from backend.services import mentor_service

router = APIRouter(prefix="/api/mentor-dashboard", tags=["Mentor Dashboard"])


@router.get("", response_model=APIResponse)
def get_mentor_dashboard(mentor_name: Optional[str] = None):
    """
    Get mentor dashboard stats + AI-generated insights.

    TODO (Interns): Currently backed by dummy data in
    backend/services/mentor_service.py — replace with real logic.
    """
    data = mentor_service.get_mentor_dashboard(mentor_name)
    return APIResponse(
    message="Mentor dashboard fetched successfully.",
    data=data
)