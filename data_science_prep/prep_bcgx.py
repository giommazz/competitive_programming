import pandas as pd
import numpy as np


"""
EXERCISE 1: given a CSV file `data.csv` with columns `id`, `value1`, `value2`:
- Load into a DataFrame
- Create a new column `value_sum` = `value1` + `value2`
- Filter rows where `value_sum` > 100 and sort them by value_sum descending
- Return the top 5 rows
"""
df = pd.read_csv("data.csv") # read csv into DataFrame
# drop NaN values to do computations
# Method 1: use `Pandas.dropna()`
# df.dropna(inplace=True)
# Method 2: use mask
mask_nan = df.isnull().any(axis=1) # Pandas Series ("any" column with NaNs is flagged)
df = df[~mask_nan] # `~` flips the Boolean mask (bitwise NOT)
df['value_sum'] = df['value1'] + df['value2']
df = df[df["value_sum"]>100]


"""
EXERCISE 2:
- Create a NumPy array of shape (100,) filled with random integers between 0 and 50 inclusive
- Replace all values less than 10 with 0.
- Compute the mean and standard deviation of the resulting array.
"""
seed = np.random.seed(42) # Set seed for reproducibility
a = np.random.randint(0, 51, size=100) # Generate array with 100 random integers
b = np.where(a >= 10, a, 0) # replace all elements <10 with 0
a_mean, a_std = a.mean(), a.std()
print(f"mean and std are: {a_mean}, {a_std}")


"""
EXERCISE 3: given two DataFrames, `df1` and `df2`,
- df1 has columns `user_id`, `score1`
- df2 has `user_id`, `score2`
- Merge them on `user_id`
- Create a new column `score_diff` = `score1` - `score2`
- From the merged DataFrame, find user_id(s) with the min absolute `score_diff`
"""
df1 = pd.read_csv("df1.csv") # read `df1`
df2 = pd.read_csv("df2.csv") # read `df2`
merged = pd.merge(df1, df2, on="user_id") # inner merge on `user_id`
merged["score_diff"] = merged["score1"] - merged["score2"] # create new column `score_diff`
print(merged)
# From `merged`, find user_id(s) with the minimum absolute `score_diff`
# two ways to do that, with `Pandas.apply` or with `Pandas.abs`
min_abs = merged["score_diff"].apply(np.absolute).min() # Compute min abs value
# Find indices corresponding rows with thaht min abs value 
min_indices = merged[merged["score_diff"].apply(np.absolute) == min_abs].index
print(merged.iloc[min_indices, :]["user_id"].values)


"""
EXERCISE 4: in a DataFrame `mixed_missing` with many missing values
- For numeric columns, replace missing values with the column mean.
- For categorical/text columns, replace missing values with the mode (most frequent).
- After filling missing values, convert all text columns to lowercase.
# """
pd.options.future.infer_string = True
mixed_missing = pd.read_csv("mixed_missing.csv")

# Method 1: hand-pick numerical and categorical columns
# `Pandas.mode()` returns a Series (plus, mode may be achieved at different elements)
#   -> grab first element through `iloc[0]`
# fill_values = {
#     'name': mixed_missing["name"].mode().iloc[0], # str
#     'city': mixed_missing["city"].mode().iloc[0], # str
#     'age': mixed_missing["age"].mean(), # float
#     'salary': mixed_missing["salary"].mean(), # float
#     'department': mixed_missing["department"].mode().iloc[0], # str
#     'join_date': mixed_missing["join_date"].mode().iloc[0] # str
#     }
# mixed_missing.fillna(value=fill_values, inplace=True)
# Method 2: use Pandas' built-in functions to select numerical and categorical columns
numeric_cols = mixed_missing.select_dtypes(include="number").columns
string_cols = mixed_missing.select_dtypes(include="str").columns
cat_cols = mixed_missing.select_dtypes(include="category").columns
mixed_missing[numeric_cols] = mixed_missing[numeric_cols].fillna(mixed_missing[numeric_cols].mean())
mixed_missing[string_cols] = mixed_missing[string_cols].fillna({c: mixed_missing[c].mode().iloc[0] for c in string_cols})
mixed_missing[cat_cols] = mixed_missing[cat_cols].fillna({c: mixed_missing[c].mode().iloc[0] for c in cat_cols})

# Same thing for the lower case question:
# Method 1: select columns manually
# str_cols = ["name", "city", "department", "join_date"]
# for col in str_cols:
#     mixed_missing[col] = mixed_missing[col].str.lower()
# Method 2: use preselected (via Pandas libraries) string columns 
mixed_missing[string_cols] = mixed_missing[string_cols].apply(lambda col: col.str.lower())


"""
EXERCISE 5: given a time-series DataFrame `df_ts` with columns `timestamp` (string in ISO format) and `value`
- Convert timestamp to Pandas datetime
- Resample data to daily frequency, computing the average value per day.
- Fill missing days by forward-fill method
"""
df_ts = pd.read_csv("df_ts.csv")
df_ts["timestamp"] = pd.to_datetime(df_ts["timestamp"])
df_ts.set_index("timestamp", inplace=True)
daily = df_ts.resample("D").mean()
daily = daily["value"].ffill()
