"""API routes for Module 5 — AI GitHub & Code Review Assistant."""

from fastapi import APIRouter
from pydantic import BaseModel
from backend.api.schemas.common import APIResponse
from backend.services import github_service

router = APIRouter(prefix="/api/github-analysis", tags=["GitHub Analyzer"])


class GitHubAnalysisRequest(BaseModel):
    repo_url: str


@router.post("", response_model=APIResponse)
def analyze_repo(payload: GitHubAnalysisRequest):
    """
    Analyze a GitHub repository submitted by an intern.

    TODO (Interns): Currently backed by dummy data in
    backend/services/github_service.py — replace with real GitHub API
    calls + AI-based scoring logic.
    """
    data = github_service.get_github_analysis(payload.repo_url)
    return APIResponse(
    message="GitHub analysis fetched successfully.",
    data=data
)
