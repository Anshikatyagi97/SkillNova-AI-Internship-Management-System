# AI Attendance & Performance Analyzer

## Purpose
Goes beyond simple attendance recording — analyses trends, predicts
drops in attendance, and produces a consistency score per intern.

## Files
- `service.py` — Core functions (see TODOs inside each function).
- `utils.py` — Small shared helper functions (e.g. streak calculation).

## AI Features To Implement
- [ ] Attendance percentage (overall / weekly / monthly)
- [ ] Consecutive absence detection
- [ ] Attendance drop prediction
- [ ] Consistency score
- [ ] Heatmap-ready data endpoint

## Suggested Approach
1. Implement the raw percentage and streak calculations first — these
   are pure data-wrangling, no AI required.
2. Add the "drop prediction" as a simple trend comparison
   (last 2 weeks vs. previous 2 weeks) before reaching for ML.
