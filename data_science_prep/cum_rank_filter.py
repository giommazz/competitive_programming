# cum_rank_filter.py
"""
Tasks:
- Convert date to datetime.
- For each category order rows by date.
- Compute a cumulative rank of score within each category up to that date: 
    for a given row, rank among all previous + current scores in that category).
- Then filter to keep only rows where the cumulative rank is ≥ 2 (i.e. not the lowest in that category up to that date).

Output should have columns: category, date, score, cum_rank.
"""

import pandas as pd
df = pd.read_csv("cum_rank_filter_input.csv")
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values(by=["category", "date"]).reset_index(drop=True)

# `groupby...().expanding()` returns multi-indexed result,
#   -> keeps track of both `category` and the original row index
#   -> `reset_index(level=0, drop=True)` drops group index (`level=0`). Needed because
#       original DataFrame only uses the plain row index
df["cum_rank"] = (
    df.groupby("category")["score"]
    .expanding()
    .rank(method="min")
    .reset_index(level=0, drop=True)
    .astype(int)
    )
df = df[df["cum_rank"]>=2][["category", "date", "score", "cum_rank"]]
print(df)