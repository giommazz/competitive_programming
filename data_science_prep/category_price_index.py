# category_price_index.py
"""
Tasks:
1. Read `price_index.csv`.
2. Convert `date` to datetime and sort by `category` + `date`.
3. For each `category`, compute a **base index** by re-scaling price so that the first date in that category has index = 100:
   index_t = price_t / price_first * 100
4. Compute **rolling 3-period growth rate** on the index (i.e. (index_t / index_{t-3} - 1)).
5. For each category, find the date with the maximum 3-period growth.
6. Output DataFrame with columns: category, date_of_max_growth, max_growth_rate
"""

import pandas as pd

# Task 1
df = pd.read_csv("data/category_price_index.csv")

# Task 2
df["date"] = pd.to_datetime(df["date"])
df.set_index("date", inplace=True)
df.sort_values(by=["category", "date"])

# Task 3
df["first_price"] = df.groupby("category")["price"].transform("first")
df["base_index"] = df["price"] / df["first_price"]* 100

# Task 4
df["growth_rate"] = (df["base_index"] / df["base_index"].shift(3) - 1).bfill()

# Task 5
# For each category, find the date with the maximum 3-period growth.
df["max_growth_rate"] = df.groupby("category")["growth_rate"].transform(lambda x: x.max())
dates = df[df["growth_rate"]==df["max_growth_rate"]].groupby("category").apply(lambda x: x.index.min()).rename("date_of_max_growth")
df = df.join(dates, on="category")
df = df[["category", "date_of_max_growth", "max_growth_rate"]]
result = (
   df.groupby("category")
   .apply(lambda x: x.iloc[0])
   .drop(columns=["category"]) # it does not drop *the index* named "category"
   .reset_index() # take current index ("category") and inserts it as a new column
   )
print(result)
