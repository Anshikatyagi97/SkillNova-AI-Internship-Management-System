# AI Internship Analytics Dashboard

## Purpose
Generates internship-wide analytics: completion rates, certificate
statistics, domain distribution, mentor workload, and an overall
program health score.

## Files
- `service.py` — Core functions (see TODOs inside each function).
- `utils.py` — Aggregation helper functions.

## AI Features To Implement
- [ ] Overall analytics aggregation
- [ ] Domain-wise intern distribution
- [ ] Mentor workload distribution
- [ ] Overall health score calculation
- [ ] AI-generated weekly summary / batch performance report

## Suggested Approach
1. Implement all raw aggregations first (pure SQL/pandas, no AI).
2. Layer the LLM-based narrative generation (weekly summary, batch
   report) on top once the raw numbers are reliable.
