# customer_visits.py

import pandas as pd

# 1. Read `customer_visits.csv`
df = pd.read_csv("data/customer_visits.csv")

# 2. Convert `visit_date` to datetime and sort by `customer_id` + `visit_date`
df["visit_date"] = pd.to_datetime(df["visit_date"])
df = df.sort_values(by=["customer_id", "visit_date"])

# 3. For each `customer_id`, compute:
# - total_visits = total number of visits
# - first_visit_date
# - last_visit_date
# - recency_days = (reference_date - last_visit_date).days
#      (Choose reference_date = 2023-12-31 for all customers)
# 4. Build a DataFrame with one row per customer and columns:
#    customer_id, total_visits, first_visit_date, last_visit_date, recency_days
def compute(df):
   d = {}
   d['total_visits'] = df['visit_date'].count()
   d['first_visit_date'] = df['visit_date'].min()
   d['last_visit_date'] = df['visit_date'].max()
   return pd.Series(d, index=['total_visits', 'first_visit_date', 'last_visit_date', 'recency_days'])
df["reference_date"] = pd.to_datetime(pd.Series(["2023-12-31"]*df.shape[0]))
result = df.groupby(by="customer_id").apply(compute)
result['recency_days'] = (pd.to_datetime("2023-12-31") - result['last_visit_date']).dt.days

# 5. Then categorize customers into three buckets (segment):
#    - "Active" if recency_days ≤ 30
#    - "At Risk" if 30 < recency_days ≤ 90
#    - "Dormant" if recency_days > 90
#    Add column `segment`.
def segmentation(row):
    if row['recency_days'] <= 30:
        return 'Active'
    elif (row['recency_days'] > 30) and (row['recency_days'] <= 90):
        return 'At Risk' 
    else:
        return 'Dormant'      
result['segment'] = result.apply(segmentation, axis=1)

# 6. Output the final DataFrame sorted by `segment` then `recency_days` ascending.
result = result.sort_values(by=["segment", "recency_days"])
print(result)