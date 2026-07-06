"""API routes for Module 3 — AI Attendance & Performance Analyzer."""

from fastapi import APIRouter
from backend.api.schemas.common import APIResponse
from backend.services import attendance_service

router = APIRouter(prefix="/api/attendance", tags=["Attendance Analyzer"])


@router.get("/{intern_id}", response_model=APIResponse)
def get_attendance(intern_id: str):
    """
    Get attendance analytics for a single intern.

    TODO (Interns): Currently backed by dummy data in
    backend/services/attendance_service.py — replace with real logic.
    """
    data = attendance_service.get_intern_attendance(intern_id)
    return APIResponse(
    message="Attendance analytics fetched successfully.",
    data=data
)