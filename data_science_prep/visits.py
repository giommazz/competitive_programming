"""
Tasks:
1. Convert date to datetime, sort by site + date.
2. For each site, compute the monthly average visits (i.e. group by site + month).
3. For each day, compute its anomaly score = (visits - monthly_avg) / monthly_std (i.e. how many standard deviations away from that month’s mean for that site).
4. Flag anomalies if |anomaly_score| > 1.
5. Return a DataFrame with site, date, visits, anomaly_score, is_anomaly (Boolean).
"""
# Imports
import pandas as pd

# Task 1
df = pd.read_csv("data/visits.csv")
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.month
df.sort_values(by=["site", "date"], inplace=True)
df.reset_index(inplace=True, drop=True)

# Task 2
grouped = df.groupby(["site", "month"])["visits"]
df["monthly_avg"], df["monthly_std"] = grouped.transform("mean"), grouped.transform("std")

# Task 3
df["anomaly_score"] = (df["visits"] - df["monthly_avg"]) / df["monthly_std"]

# Task 4
# Equivalently: `df["is_anomaly"] = df["anomaly_score"].abs() > 1`
df["is_anomaly"] = df.apply(lambda x: True if abs(x["anomaly_score"]) > 1 else False, axis=1)


df = df[["site", "date", "visits", "anomaly_score", "is_anomaly"]]