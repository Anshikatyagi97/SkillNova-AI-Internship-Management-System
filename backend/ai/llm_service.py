"""
Common LLM Service using Groq.

This file acts as the single AI gateway for the entire project.
All AI modules should call this service instead of directly
calling the Groq API.
"""

from groq import Groq

from backend.config.settings import settings


SYSTEM_PROMPT = """
You are SkillNova AI Mentor.

You help mentors and interns by generating:
- Internship progress summaries
- Attendance insights
- Performance feedback
- Certificate eligibility explanations
- GitHub repository reviews
- Task recommendations

Always provide concise, professional, and encouraging responses.
"""


class LLMService:

    def __init__(self):

        if not settings.GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY not found in .env")

        self.client = Groq(api_key=settings.GROQ_API_KEY)

    def generate_response(
        self,
        prompt: str,
        model: str = "llama-3.3-70b-versatile",
    ) -> str:

        try:

            response = self.client.chat.completions.create(
                model=model,
                temperature=0.3,
                max_tokens=512,
                messages=[
                    {
                        "role": "system",
                        "content": SYSTEM_PROMPT,
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    },
                ],
            )

            return response.choices[0].message.content.strip()

        except Exception as e:
            print(f"Groq Error: {e}")
            return "Unable to generate AI response at the moment."


llm = LLMService()