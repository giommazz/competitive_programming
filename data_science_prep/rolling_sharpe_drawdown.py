# rolling_sharpe_drawdown.py

"""
1.  Convert `date` to datetime and sort by `asset` + `date`.
2.  For each asset, compute a rolling 3-day Sharpe ratio of returns (assume risk-free = 0).
    Use rolling window size = 3, compute mean / std of returns in window, Sharpe = mean / std.
3.  For each asset, compute drawdown as the maximum drop from a historical peak up to that date, 
    i.e. running peak of cumulative return minus current cumulative return).
4.  Return a DataFrame with asset, date, rolling_sharpe, drawdown.
"""

# imports
import pandas as pd

# Task 1
df = pd.read_csv("data/rolling_sharpe_drawdown.csv")
df["date"] = pd.to_datetime(df["date"])
df.sort_values(by=["asset", "date"], inplace=True)

# Task 2
df["rolling_mean"] = (
    df.groupby("asset")["return"]
    .rolling(window=3, min_periods=1)
    .mean()
    .reset_index(level=0, drop=True)
    )
df["rolling_std"] = (
    df.groupby("asset")["return"]
    .rolling(window=3, min_periods=1)
    .std(ddof=0)
    .reset_index(level=0, drop=True)
    )
df["rolling_sharpe"] = df["rolling_mean"] / df["rolling_std"]
df.drop(["rolling_mean", "rolling_std"], inplace=True, axis=1)

# Task 3
df["cum_return"] = (
    df.groupby("asset")["return"]
    .cumsum() # same as `.expanding().sum()`
    .reset_index(level=0, drop=True)
    )

df["drawdown"] = df.groupby("asset")["cum_return"].cummax() - df["cum_return"]
df.drop(["return", "cum_return"], inplace=True, axis=1)
df = df[["asset", "date", "rolling_sharpe", "drawdown"]]

print(df)