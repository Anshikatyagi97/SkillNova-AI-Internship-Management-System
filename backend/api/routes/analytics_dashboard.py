"""API routes for Module 7 — AI Internship Analytics Dashboard."""

from fastapi import APIRouter
from backend.api.schemas.common import APIResponse
from backend.services import analytics_service

router = APIRouter(prefix="/api/analytics", tags=["Analytics Dashboard"])


@router.get("", response_model=APIResponse)
def get_analytics():
    """
    Get platform-wide internship analytics + AI-generated insights.

    TODO (Interns): Currently backed by dummy data in
    backend/services/analytics_service.py — replace with real logic.
    """
    data = analytics_service.get_platform_analytics()
    return APIResponse(
    message="Analytics fetched successfully.",
    data=data
)