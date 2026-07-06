"""
SkillNova AI-Powered Internship Management & Mentor Intelligence System
Backend entry point.

Run with:
    uvicorn backend.main:app --reload

Then visit:
    http://127.0.0.1:8000/docs   (interactive Swagger UI)

TODO (Interns):
- Add authentication/authorization (e.g. JWT) before exposing this
  publicly or integrating with the SkillNova web platform.
- Add a global exception handler.
- Add request logging middleware.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.config.settings import settings
from backend.api.routes import (
    progress_tracker,
    mentor_dashboard,
    attendance,
    task_recommendation,
    github_analysis,
    certificate_analysis,
    analytics_dashboard,
)

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=(
        "AI-powered backend services for the SkillNova Internship Platform. "
        "This is a STARTER TEMPLATE — most AI logic is intentionally left as "
        "TODOs for interns to implement. See README.md for details."
    ),
)

# CORS - allow the Streamlit frontend (and eventually the SkillNova web app)
# to call these APIs during local development.
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register all module routers
app.include_router(progress_tracker.router)
app.include_router(mentor_dashboard.router)
app.include_router(attendance.router)
app.include_router(task_recommendation.router)
app.include_router(github_analysis.router)
app.include_router(certificate_analysis.router)
app.include_router(analytics_dashboard.router)


@app.get("/", tags=["Health"])
def root():
    """Basic health-check / welcome endpoint."""
    return {
        "message": f"{settings.APP_NAME} is running.",
        "version": settings.APP_VERSION,
        "docs": "/docs",
        "status": "ok — this is a starter template with dummy data. See README.md for TODOs.",
    }


@app.get("/health", tags=["Health"])
def health_check():
    """Health-check endpoint for monitoring / uptime checks."""
    return {"status": "healthy"}
