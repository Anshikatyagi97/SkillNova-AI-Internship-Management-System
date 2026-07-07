"""
AI Task Recommendation System - Service Layer

TODO (Interns):
1. Implement `identify_weak_skills()` based on low scores / late submissions
   grouped by task domain/topic.
2. Implement `recommend_tasks()` - suggest the next practice tasks/projects.
3. Implement `recommend_learning_resources()` - courses, reading material,
   revision topics (can be a static curated mapping to start with, or
   RAG-based retrieval from a vector DB of learning resources).
"""

from typing import Dict, List
from backend.ai.llm_service import llm


def identify_weak_skills(intern_id: str) -> List[str]:
    """
    Identify skill areas where an intern is underperforming.

    TODO: Analyze Submission scores + MentorFeedback grouped by
          Task.domain to find the weakest areas.
    """
    return []


def recommend_tasks(intern_id: str) -> List[Dict]:
    """
    Recommend personalized practice tasks / projects.

    TODO: Use completed tasks + weak skills + current domain to
          pick the next 3-5 tasks from the Task table.
    """
    return []


def recommend_learning_resources(intern_id: str) -> Dict:
    """
    Recommend courses, reading material, and revision topics.

    TODO: Start with a static curated dictionary keyed by domain/skill.
          Later, upgrade to a RAG pipeline: embed learning resources into
          ChromaDB/FAISS, then retrieve the most relevant ones for the
          intern's weak skills.
    """
    return {
        "courses": [],
        "practice_tasks": [],
        "projects": [],
        "reading_material": [],
        "revision_topics": [],
    }

def generate_ai_task_recommendations(
    intern_id: str,
    weak_skills: List[str],
) -> str:
    """
    Generate AI-powered learning recommendations.
    """

    prompt = f"""
You are an AI Internship Mentor.

Intern ID: {intern_id}

Weak Skills:
{', '.join(weak_skills) if weak_skills else 'None'}

Generate personalized recommendations.

Include:
1. Skills to improve
2. Practice strategy
3. Project suggestion
4. Motivation

Keep it concise (3-5 sentences).
"""

    return llm.generate_response(prompt)


def recommend_courses(
    weak_skills: List[str],
) -> List[str]:
    """
    Recommend courses based on weak skills.
    """

    mapping = {
        "Python": "Python for Everybody",
        "FastAPI": "FastAPI Complete Guide",
        "SQL": "SQL for Data Analysis",
        "Machine Learning": "Machine Learning Specialization",
        "Git": "Git & GitHub Bootcamp",
    }

    recommendations = []

    for skill in weak_skills:
        if skill in mapping:
            recommendations.append(mapping[skill])

    if not recommendations:
        recommendations.append("Complete Internship Foundation Course")

    return recommendations


def recommend_projects(
    weak_skills: List[str],
) -> List[str]:
    """
    Recommend projects based on weak skills.
    """

    if "FastAPI" in weak_skills:
        return [
            "Build a REST API",
            "Student Management System",
        ]

    if "Machine Learning" in weak_skills:
        return [
            "House Price Prediction",
            "Spam Detection",
        ]

    return [
        "Personal Portfolio",
        "Task Management App",
    ]