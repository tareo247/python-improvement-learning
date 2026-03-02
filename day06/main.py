import pandas as pd

df = pd.read_csv("attendance.csv")

print(df)

print(type(df))
print(df.columns)
print(df.dtypes)

df["start_time"] = pd.to_datetime(df["start_time"], format="%H:%M")
df["end_time"]   = pd.to_datetime(df["end_time"], format="%H:%M")

df["work_hours"] = (df["end_time"] - df["start_time"]).dt.total_seconds() / 3600

print(df)

# employee_id ごとの総勤務時間
total_hours = df.groupby("employee_id")["work_hours"].sum()

print(total_hours)

import datetime

# 遅刻基準 09:00
threshold = pd.to_datetime("09:00", format="%H:%M").time()

# 遅刻した社員IDを抽出
df["start_time_only"] = df["start_time"].dt.time
late_employees = df[df["start_time_only"] > threshold]["employee_id"].unique()

print("遅刻者:", late_employees)

# 残業基準
OVERTIME_THRESHOLD = 8

overtime_employees = df[df["work_hours"] >= OVERTIME_THRESHOLD]["employee_id"].unique()
print("残業者:", overtime_employees)

# 記録漏れ（start_time または end_time が欠損している行を抽出）
no_record_employees = df[df["start_time"].isna() | df["end_time"].isna()]["employee_id"].unique()
print("記録漏れ:", no_record_employees)