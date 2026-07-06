"""API routes for Module 6 — AI Certificate Eligibility Analyzer."""

from fastapi import APIRouter
from backend.api.schemas.common import APIResponse
from backend.services import certificate_service

router = APIRouter(prefix="/api/certificate", tags=["Certificate Analyzer"])


@router.get("/{intern_id}", response_model=APIResponse)
def get_certificate_status(intern_id: str):
    """
    Get certificate eligibility status + explanation for an intern.

    TODO (Interns): Currently backed by dummy data in
    backend/services/certificate_service.py — replace with real logic.
    """
    data = certificate_service.get_certificate_eligibility(intern_id)
    return APIResponse(
    message="Certificate eligibility fetched successfully.",
    data=data
)