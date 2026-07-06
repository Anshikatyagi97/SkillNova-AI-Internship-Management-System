# AI Task Recommendation System

## Purpose
Recommends personalized tasks, courses, and revision material based
on an intern's completed work, weak skills, and current domain.

## Files
- `service.py` — Core functions (see TODOs inside each function).
- `utils.py` — Prompt-building / RAG helper functions.

## AI Features To Implement
- [ ] Weak skill identification
- [ ] Task recommendation
- [ ] Learning resource recommendation (courses, projects, reading material)

## Suggested Approach
1. Start with a static rules/mapping table (domain → recommended tasks).
2. Layer a RAG pipeline on top using ChromaDB or FAISS if you want
   resource recommendations to scale beyond a hardcoded list.
