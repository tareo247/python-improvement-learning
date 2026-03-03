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

# 社員別 総勤務時間・平均勤務時間
summary = df.groupby("employee_id")["work_hours"].agg(["sum", "mean"])
print(summary)

df["is_overtime"] = df["work_hours"] >= OVERTIME_THRESHOLD

overtime_count = df.groupby("employee_id")["is_overtime"].sum()
print(overtime_count)

threshold = pd.to_datetime("09:00", format="%H:%M").time()

df["is_late"] = df["start_time"].dt.time > threshold

late_count = df.groupby("employee_id")["is_late"].sum()
print(late_count)

problem_employees = df[
    (df["is_overtime"]) | (df["is_late"])
]["employee_id"].unique()

print("改善対象:", problem_employees)

# lambda practice
practice1 = lambda x: (x >= 10)
print(practice1(9))

practice2 = lambda y: y * y
print(practice2(12))

practice3 = lambda z: "High" if z >= 5 else "Low"
print(practice3(7))

# list 順序あり　変更可能
numbers = [1, 2, 3, 4]

print(numbers)
print(numbers[0])
print(numbers[-1])

numbers.append(5)
numbers.remove(2)
print(numbers)

for n in numbers:
    print(n)

practice_list = [2, 5, 8, 11, 14]
practice5 = list(filter(lambda x: x % 2 == 0, practice_list))
print(practice5)

practice6 = list(map(lambda x: x * 3, practice_list))
print(practice6)

practice7 = list(map(lambda x: x * x if x > 5 else x, practice_list))
print(practice7)

