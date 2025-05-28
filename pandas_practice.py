# pandas_practice.py
import pandas as pd

# create a Series with given data and labels
data = ["apple", "banana", "cherry", "date"]
series = pd.Series(data=data, index = ["A", "B", "C", "D"])

# now convert `series` into a DataFrame with one column labeled "fruit"
df = pd.DataFrame(series, columns=["fruit"])

# add a second column "length" to `df` containing the length of each fruit name
df["length"] = pd.Series([len(f) for f in data], index=df.index)
# the following would work too
df["length"] = df["fruit"].str.len()

# Select the rows where length > 5 and return them as a new DataFrame `df_long`
df_long = df[df["length"] > 5]

# reset index, replaces row names with integers 0, 1, 2, ... 
df_long = df_long.reset_index(drop=True)
# One obtains the same result by running 
#   `df_long.reset_index(drop=True, inplace=True)`
#   which modifies `df_long` in place