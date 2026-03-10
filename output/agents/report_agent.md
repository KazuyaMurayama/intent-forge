# Report Agent

## Role
Report generation and result validation.

## Max Turns
3

## STEP 3: REPORT

Run `src/report.py` to generate `REPORT.md` from `data/results.json`:
- Executive summary with top recommendations
- Full ranking table
- Key findings and patterns
- Methodology notes

## STEP 4: REVIEW

Validate:
- All data files exist in `data/`
- Results JSON has all required fields
- Report covers top 5 candidates
- No file exceeds 200 lines

Output summary to console.
