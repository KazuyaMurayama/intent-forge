# NASDAQ DIVERSIFICATION ANALYZER

On user input, execute steps 1-4. Load agent from `agents/{name}.md` per step. Update `state/session.json` after each step.

## Pipeline

1. **FETCH** → `data_agent` → Download daily data from Yahoo Finance → `data/`
2. **ANALYZE** → `data_agent` → Correlation matrix, returns, diversification scoring
3. **REPORT** → `report_agent` → Generate findings report
4. **REVIEW** → `report_agent` → Validate results, output summary

## Error Convention

On error: append `{ "step": N, "agent": "", "message": "" }` to `state/session.json` `errors[]` and continue.

## Constraints

- Agents: 2 | Turns/agent ≤ 3 | Steps: 4
- Data source: Yahoo Finance (yfinance)
- This file: routing logic only
