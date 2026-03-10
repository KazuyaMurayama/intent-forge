"""Analyze correlations and returns vs NASDAQ."""
import pandas as pd
import numpy as np
import json
import os

NAMES = {
    "^IXIC": "NASDAQ Composite", "^GSPC": "S&P 500", "^DJI": "Dow Jones",
    "^RUT": "Russell 2000", "^N225": "Nikkei 225", "^FTSE": "FTSE 100",
    "^GDAXI": "DAX", "^FCHI": "CAC 40", "^HSI": "Hang Seng",
    "^BSESN": "BSE Sensex", "^BVSP": "Bovespa", "GLD": "Gold ETF",
    "TLT": "US Treasury 20Y+ ETF", "VNQ": "US Real Estate ETF",
    "EEM": "Emerging Markets ETF", "DBC": "Commodities ETF",
}


def analyze():
    close = pd.read_csv("data/daily_closes.csv", index_col=0, parse_dates=True)
    daily_ret = close.pct_change().dropna()

    # Correlation matrix
    corr_matrix = daily_ret.corr()
    corr_matrix.to_csv("data/correlation_matrix.csv")

    nasdaq_ret = daily_ret["^IXIC"]
    results = []

    for ticker in daily_ret.columns:
        if ticker == "^IXIC":
            continue
        ret = daily_ret[ticker]
        aligned = pd.concat([nasdaq_ret, ret], axis=1).dropna()
        corr = aligned.iloc[:, 0].corr(aligned.iloc[:, 1])
        total_return = (1 + ret).prod() - 1
        years = len(ret) / 252
        ann_ret = (1 + total_return) ** (1 / years) - 1
        ann_vol = ret.std() * np.sqrt(252)
        sharpe = ann_ret / ann_vol if ann_vol > 0 else 0

        results.append({
            "ticker": ticker,
            "name": NAMES.get(ticker, ticker),
            "correlation_with_nasdaq": round(corr, 4),
            "annual_return_pct": round(ann_ret * 100, 2),
            "annual_volatility_pct": round(ann_vol * 100, 2),
            "sharpe_ratio": round(sharpe, 4),
        })

    df = pd.DataFrame(results)
    # Diversification score
    c = df["correlation_with_nasdaq"]
    r = df["annual_return_pct"]
    c_norm = 1 - (c - c.min()) / (c.max() - c.min())
    r_norm = (r - r.min()) / (r.max() - r.min())
    df["diversification_score"] = round(c_norm * 0.5 + r_norm * 0.5, 4)
    df = df.sort_values("diversification_score", ascending=False)

    nasdaq_total = (1 + nasdaq_ret).prod() - 1
    nasdaq_ann = (1 + nasdaq_total) ** (1 / (len(nasdaq_ret) / 252)) - 1

    output = {
        "all_indices": df.to_dict(orient="records"),
        "top_candidates": df.head(5).to_dict(orient="records"),
        "nasdaq_annual_return_pct": round(nasdaq_ann * 100, 2),
        "analysis_period": "5 years",
        "data_source": "Yahoo Finance",
    }

    os.makedirs("data", exist_ok=True)
    with open("data/results.json", "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print("✅ Saved analysis to data/results.json")
    return output


if __name__ == "__main__":
    analyze()
