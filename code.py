import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
# Inputs
stocks = {
    "INFY.NS": "Infosys.Ltd",
    "TCS.NS": "TCS.Ltd",
    "HCLTECH.NS": "HCL.Ltd",
    "WIPRO.NS": "WIPRO",
    "PERSISTENT.NS": "Persistent Systems"
}
start_date = "2025-04-01"
end_date = "2026-04-01"
# Downloading data

prices = yf.download(
    list(stocks.keys()),
    start=start_date,
    end=end_date,
    progress=False
)["Close"]
prices = prices.dropna(axis=1, how="all")
# Rebasing
indexed = prices.apply(lambda x: x / x.dropna().iloc[0] * 100)
# Plotting

plt.figure(figsize=(11, 6))
for ticker, name in stocks.items():
    if ticker in indexed.columns:
        plt.plot(indexed.index, indexed[ticker], linewidth=2.2, label=name)
plt.axhline(100, linestyle=":", linewidth=1)
plt.title("Peer Performance – 1Y (Indexed)", fontsize=15, fontweight="bold")
plt.ylabel("Indexed Value")
plt.xlabel("Date")
plt.grid(True, linestyle="--", alpha=0.4)
plt.legend(frameon=False, ncol=2)
for spine in ["top", "right"]:
    plt.gca().spines[spine].set_visible(False)
plt.tight_layout()
plt.show()
