# AI Internship Progress Tracker

## Purpose
Continuously monitors each intern's internship journey: task completion,
submission history, pending/late tasks, and overall progress percentage.

## Files
- `service.py` — Core functions (see TODOs inside each function).
- `utils.py` — Small helper functions shared within this module.

## AI Features To Implement
- [ ] Predict slow progress (`predict_slow_progress`)
- [ ] Detect inactive interns (`detect_inactive_interns`)
- [ ] Generate natural-language progress summaries (`generate_ai_progress_narrative`)
- [ ] Suggest next tasks (`suggest_next_tasks`)

## Suggested Approach
1. Start with rule-based logic (thresholds on completion %, days inactive).
2. Once rule-based logic works end-to-end, replace with a trained
   Scikit-learn model or an LLM call where appropriate.
3. Keep the function signatures unchanged so the backend `services/`
   layer and Streamlit frontend keep working without modification.
