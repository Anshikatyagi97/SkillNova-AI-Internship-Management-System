# AI Mentor Dashboard

## Purpose
Helps mentors manage large numbers of interns by surfacing key
statistics plus AI-generated natural-language insights and alerts.

## Files
- `service.py` — Core functions (see TODOs inside each function).
- `utils.py` — Small shared helper functions.

## AI Features To Implement
- [ ] Dashboard statistics aggregation (`get_dashboard_stats`)
- [ ] Top / weak performer ranking
- [ ] AI-generated alerts (`generate_ai_alerts`)
- [ ] AI-generated mentor recommendations

## Example Insight Output (target behaviour)
> "12 interns are falling behind due to missing weekly submissions."
> "Most interns are struggling with Backend Development tasks."

## Suggested Approach
1. Compute the raw numbers first (rule-based aggregation).
2. Feed the raw numbers into an LLM prompt template to produce the
   natural-language sentence. Keep the prompt short and structured.
