# Data Agent

## Role
Data fetching, correlation analysis, diversification scoring.

## Max Turns
3

## STEP 1: FETCH

Download 5-year daily close prices from Yahoo Finance via `src/fetch_data.py`.

Tickers: ^IXIC (NASDAQ), ^N225, ^FTSE, ^GDAXI, ^FCHI, ^HSI, ^BSESN, ^BVSP, GLD, TLT, VNQ, EEM, DBC, ^GSPC, ^DJI, ^RUT.

Output: `data/daily_closes.csv`

## STEP 2: ANALYZE

Run `src/analyze.py`:
1. Compute daily returns
2. Calculate pairwise correlation with NASDAQ
3. Calculate annualized return, volatility, Sharpe ratio per index
4. Score: diversification_score = 0.5 * (1 - corr_normalized) + 0.5 * return_normalized
5. Rank by score, identify top 5 candidates

Output: `data/results.json`, `data/correlation_matrix.csv`
