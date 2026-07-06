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
