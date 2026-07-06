"""
Application configuration settings.

Loads environment variables (via python-dotenv) and exposes a single
`settings` object that the rest of the backend imports from.

TODO (Interns):
- Add validation for required environment variables.
- Add separate settings profiles for development / testing / production.
"""

import os
from dotenv import load_dotenv

# Load variables from a .env file if present
load_dotenv()


class Settings:
    """Central configuration object for the whole backend."""

    # --- General ---
    APP_NAME: str = os.getenv("APP_NAME", "SkillNova AI Internship Management System")
    APP_VERSION: str = os.getenv("APP_VERSION", "0.1.0")
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    DEBUG: bool = os.getenv("DEBUG", "True").lower() == "true"

    # --- Database ---
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./skillnova.db")

    # --- AI / LLM providers (placeholders only, no keys committed) ---
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")

    # --- Vector DB (for future RAG-based modules) ---
    VECTOR_DB_PROVIDER: str = os.getenv("VECTOR_DB_PROVIDER", "chromadb")
    VECTOR_DB_PATH: str = os.getenv("VECTOR_DB_PATH", "./vector_store")

    # --- CORS ---
    ALLOWED_ORIGINS: list = os.getenv("ALLOWED_ORIGINS", "*").split(",")

    # TODO (Interns): Add pagination defaults, rate-limit config, logging level, etc.


settings = Settings()
