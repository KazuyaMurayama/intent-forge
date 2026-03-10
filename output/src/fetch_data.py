"""Fetch 5-year daily close prices from Yahoo Finance."""
import yfinance as yf
import os

TICKERS = {
    "^IXIC": "NASDAQ Composite",
    "^GSPC": "S&P 500",
    "^DJI": "Dow Jones",
    "^RUT": "Russell 2000",
    "^N225": "Nikkei 225",
    "^FTSE": "FTSE 100",
    "^GDAXI": "DAX",
    "^FCHI": "CAC 40",
    "^HSI": "Hang Seng",
    "^BSESN": "BSE Sensex",
    "^BVSP": "Bovespa",
    "GLD": "Gold ETF",
    "TLT": "US Treasury 20Y+ ETF",
    "VNQ": "US Real Estate ETF",
    "EEM": "Emerging Markets ETF",
    "DBC": "Commodities ETF",
}


def fetch():
    os.makedirs("data", exist_ok=True)
    data = yf.download(
        list(TICKERS.keys()), period="5y", interval="1d", auto_adjust=True
    )
    close = data["Close"].ffill().dropna()
    close.to_csv("data/daily_closes.csv")
    print(f"✅ Saved {len(close)} rows x {len(close.columns)} tickers to data/daily_closes.csv")
    return close


if __name__ == "__main__":
    fetch()
