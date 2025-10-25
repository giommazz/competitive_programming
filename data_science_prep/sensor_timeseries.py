# sensor_timeseries.py

import pandas as pd
import numpy as np

# 1. Read `data/sensor_timeseries.csv`.
df = pd.read_csv("data/sensor_timeseries.csv")

# 2. Convert `timestamp` to datetime and sort by `sensor_id` + `timestamp`.
df["timestamp"] = pd.to_datetime(df["timestamp"])
df = df.sort_values(by=["sensor_id", "timestamp"])

# 3. For each sensor_id, create a numpy array of its 'value' column.
sensor_distinct = df["sensor_id"].unique() # returns list
sensor_values = []
for sensor in sensor_distinct:
    sensor_values.append(np.array(df[df["sensor_id"] == sensor]["value"].to_list()))

# 4. Using NumPy, compute for each sensor:
#    - mean_value
#    - std_dev
#    - z_scores = (value – mean_value) / std_dev
means, stds = [], []
z = []
for sensor in sensor_values:
    sensor_mean, sensor_std = np.mean(sensor), np.std(sensor)
    means.append(sensor_mean)
    stds.append(sensor_std)
    z.append((sensor - sensor_mean)/sensor_std)

# 5. Convert the z_scores array back into a new column in the DataFrame: 'z_score'.
z_concat = np.concatenate(z) # concatenate the two sensor arrays
df["z_score"] = pd.Series(z_concat)

# 6. Then, with pandas, for each sensor_id compute:
#    - count_high = number of z_scores > 2
#    - pct_high = count_high / total_count
#    - max_z = maximum z_score
def compute(df):
    print(df.columns)
    d = {}
    d["count_high"] = df[df["z_score"] > 2]["z_score"].count()
    d["max_z"] = df["z_score"].max()
    d["tot_count"] = df["z_score"].count()
    return pd.Series(d, index=["count_high", "max_z", "tot_count"])
result = df.groupby(by="sensor_id").apply(compute)
result["pct_high"] = result["count_high"] / result["tot_count"]
result["mean_value"] = pd.Series(means, index=result.index)
result["std_dev"] = pd.Series(stds, index=result.index)

# 7. Output a summary DataFrame with columns:
#    sensor_id, mean_value, std_dev, count_high, pct_high, max_z
result = result[["mean_value", "std_dev", "count_high", "pct_high", "max_z"]]
print(result)