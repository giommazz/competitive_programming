# cum_growth_ranking.py
"""
1. Convert year to integer (if needed) and sort by country + year.
2. Compute yearly growth rate per country (for each year after the first):
    growth_t = gdp_t/gdp_{t-1} - 1
   For the first year for each country, growth = NaN.
3. Compute cum. growth from the first available year for each country up to each year:
    cum_growth_t = Prod_{s = year_0 + 1}^t (1 + growth_s) - 1
4. At the latest year observed for each country, compute a rank across countries by their cumulative growth (highest growth = rank 1).
5. Return a DataFrame with columns: country, year, gdp, growth, cum_growth, final_rank.
The `final_rank` only populated for the most recent year of each country (others can be NaN).
"""
import pandas as pd
import numpy as np

# Task 1
df = pd.read_csv("data/growth.csv")
df["year"] = df["year"].astype(int)
df.sort_values(by=["country", "year"], inplace=True)

# Task 2
df["growth"] = df.groupby(by="country")["gdp"].transform(lambda x: x / x.shift(1) - 1)

# Task 2
df["cum_growth"] = (
    df.groupby(by=["country"])["growth"]
    .expanding()
    .agg(lambda x: x.prod()-1)
    .droplevel(0)
    )

# Task 4
ranks = df.groupby(by=["country"])["cum_growth"].last().rank(ascending=False).astype(int).rename("final_rank")
df = df.join(ranks, on="country")
print(df)
max_year = df.groupby("country")["year"].transform("max")
df.loc[df["year"] != max_year, "final_rank"] = np.nan
print(df)
