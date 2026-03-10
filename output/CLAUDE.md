# NASDAQ DIVERSIFICATION ANALYZER

On user input, execute steps 1-4. Update `state/session.json` after each step.

## Pipeline

1. **FETCH** → `data_agent` → `python src/fetch_data.py` → Yahoo Finance 5Yデイリーデータ取得 → `data/daily_closes.csv`
2. **ANALYZE** → `data_agent` → `python src/analyze.py` → 相関・リターン・分散スコア算出 → `data/results.json`
3. **REPORT** → `report_agent` → `python src/report.py` → `REPORT.md` 生成
4. **REVIEW** → `report_agent` → 結果検証、サマリー出力

## Setup

初回: `pip install -r requirements.txt`

## Error Convention

On error: append `{ "step": N, "agent": "", "message": "" }` to `state/session.json` `errors[]` and continue.

## Constraints

- Agents: 2 | Turns/agent ≤ 3 | Steps: 4
- Data: Yahoo Finance 5年デイリー終値（調整後）
- 対象: 15インデックス/ETF vs NASDAQ
- Score: `0.5 × (1-相関正規化) + 0.5 × リターン正規化`
- This file: routing logic only
