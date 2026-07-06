# AI Certificate Eligibility Analyzer

## Purpose
Automatically determines whether an intern is Eligible, Not Eligible,
or Needs Improvement for their completion certificate, with a
supporting explanation.

## Files
- `service.py` — Core functions (see TODOs inside each function).
- `utils.py` — Weighted scoring helper.

## AI Features To Implement
- [ ] Eligibility evaluation combining attendance, completion,
      submissions, mentor feedback, and GitHub activity
- [ ] Natural-language explanation generation

## Suggested Approach
1. Define clear numeric thresholds first (rule-based decision tree).
2. Once the rule-based version works, add an LLM call purely for
   generating the human-readable explanation — keep the actual
   eligibility *decision* rule-based and auditable.
