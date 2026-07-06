# AI GitHub & Code Review Assistant

## Purpose
Analyses GitHub repositories submitted by interns: commit history,
README quality, documentation, and overall code quality.

## Files
- `service.py` — Core functions (see TODOs inside each function).
- `utils.py` — URL-parsing / GitHub API helper functions.

## AI Features To Implement
- [ ] Repository analysis (commits, branches, structure)
- [ ] README quality scoring
- [ ] Code quality scoring
- [ ] Natural-language Git/GitHub improvement suggestions

## Suggested Approach
1. Use the public GitHub REST API (unauthenticated calls are rate
   limited — consider adding a personal access token via `.env`).
2. Start with simple heuristics (README length, commit count) before
   reaching for LLM-based grading.
