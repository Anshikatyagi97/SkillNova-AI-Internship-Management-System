"""
Common LLM Service

This file acts as a single entry point for all AI modules.

Currently:
- Rule-based fallback

Future:
- Gemini API
- Groq
- OpenAI
"""

from backend.config.settings import settings


class LLMService:

    def generate_response(self, prompt: str) -> str:
        """
        Temporary placeholder.

        Sprint 11 Phase 2:
        Replace this with Gemini API.
        """

        return (
            "AI Response Placeholder:\n\n"
            + prompt
        )


llm = LLMService()