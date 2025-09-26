import pandas as pd
import numpy as np


"""
EXERCISE 1: sliding window / rolling statistics + outlier detection
Given `sensor_readings.csv` with columns `timestamp` (ISO string), `sensor_id`, `reading_value`, solve the following:
- Convert timestamp to datetime and set index (or sort).
- For each sensor_id, compute a 1-hour rolling mean and rolling standard deviation (assuming irregular intervals).
- Flag readings as outliers if the reading_value is more than 2 standard deviations away from the rolling mean (within that sensor_id).
- Return a DataFrame with all outliers: columns sensor_id, timestamp, reading_value, rolling_sensor_mean, rolling_sensor_std.
"""
# df = pd.read_csv("sensor_readings.csv")
# df["timestamp"] = pd.to_datetime(df["timestamp"])
# df.set_index("timestamp", inplace=True)
# df.sort_index(inplace=True)
# df["rolling_sensor_mean"] = df.groupby("sensor_id")["reading_value"].transform(lambda s: s.rolling("1h", min_periods=1).mean())
# df["rolling_sensor_std"] = df.groupby("sensor_id")["reading_value"].transform(lambda s: s.rolling("1h", min_periods=1).std(ddof=0))
# df["sensor_std"] = df.groupby("sensor_id")["reading_value"].transform(lambda s: s.std(ddof=0))
# outlier_mask = (np.abs(df["reading_value"] - df["rolling_sensor_mean"]) > 2 * df["rolling_sensor_std"])
# outliers = df.loc[outlier_mask, 
#         [
#         "sensor_id",
#         "reading_value",
#         "rolling_sensor_mean",
#         "rolling_sensor_std",
#         ]
# ]
# outliers = outliers.reset_index()  # brings timestamp back as a column
# if len(outliers) > 0:
#     print(outliers.shape)
# else:
#     print("No outliers!")


"""
EXERCISE 2: Pivot / reshape + missing combination handling
Given `sales.csv` with columns `region`, `product`, `month` (YYYY-MM), `units_sold`, solve the following
- Load the data.
- Pivot into a DataFrame with `region` as rows, `product` as columns, `values` = sum of units_sold per region-product-month.
- For missing region-product for some months, fill with 0.
- Then compute, per region, the product with highest growth from the first month to the last month (i.e. (units_last - units_first) / units_first). If first month has 0 units, define growth as NaN or skip.
- Tricky parts: months missing entirely, division by zero, handling zeros vs missing, multiple aggregation months, sorting months.
"""
sales = pd.read_csv("sales.csv")
pivot = sales.pivot_table(
    index="region", # rows
    columns=["product", "month"], # columns (multi-level)
    values="units_sold", # numbers to aggregate
    aggfunc="sum",
    fill_value=0, # replace missing combos with 0
)

pivot.sort_index(axis=1, level=["product", "month"], inplace=True)  # sort columns so first/last month lookups stay consistent
months = sales["month"].sort_values().unique()  # capture distinct months in chronological order
first_month, last_month = months[0], months[-1]  # pick earliest and latest month present in the data
first_vals = pivot.xs(first_month, level="month", axis=1)  # slice pivot to get first-month totals per region/product
last_vals = pivot.xs(last_month, level="month", axis=1)  # slice pivot to get last-month totals per region/product
denom = first_vals.replace(0, np.nan)  # avoid divide-by-zero by treating zero baselines as missing
growth = (last_vals - first_vals) / denom  # compute growth rate from first to last month per region/product
best_product = growth.idxmax(axis=1)  # locate product with highest growth for each region
best_growth = growth.max(axis=1)  # record the actual growth rate for that product per region
growth_summary = pd.DataFrame(
    {"best_product": best_product, "growth_rate": best_growth}
)  # assemble a compact summary table per region
print(growth_summary)  # inspect the per-region best performers and their growth rates

