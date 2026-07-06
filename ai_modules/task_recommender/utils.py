"""Helper utilities for the Task Recommendation AI module."""


# TODO (Interns): If you build a RAG-based recommender, put your
# ChromaDB/FAISS client setup and embedding helper functions here.
def build_recommendation_prompt(intern_summary: dict) -> str:
    """
    Build the LLM prompt used to generate personalized recommendations
    from a structured intern summary dict.

    TODO: Design a clear, structured prompt template. Keep it short and
          include only the fields the model actually needs.
    """
    return f"TODO: build a prompt using {intern_summary}"
