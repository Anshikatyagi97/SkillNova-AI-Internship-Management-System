"""API routes for Module 4 — AI Task Recommendation System."""

from fastapi import APIRouter
from backend.api.schemas.common import APIResponse
from backend.services import task_service

router = APIRouter(prefix="/api/task-recommendations", tags=["Task Recommendation"])


@router.get("/{intern_id}", response_model=APIResponse)
def get_recommendations(intern_id: str):
    """
    Get personalized task/course/resource recommendations for an intern.

    TODO (Interns): Currently backed by dummy data in
    backend/services/task_service.py — replace with real logic.
    """
    data = task_service.get_task_recommendations(intern_id)
    return APIResponse(message="Task recommendations fetched successfully.", data=data)
