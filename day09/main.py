import sqlite3

# DB接続（なければ作られる）
conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

# テーブル作成
cursor.execute("""
-- 勤怠テーブル
CREATE TABLE IF NOT EXISTS attendance (
    employee_id INTEGER,
    date TEXT,
    start_time TEXT,
    end_time TEXT,
    work_hours REAL
)
""")
cursor.execute("""
-- 部署テーブル
CREATE TABLE IF NOT EXISTS department (
    employee_id INTEGER,
    department TEXT
);
""")

conn.commit()

# int
cursor.execute("""
    DELETE FROM attendance
""")

cursor.execute("""
    DELETE FROM department
""")
conn.commit()

# CSV Read
import csv

with open("attendance.csv", mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        # データ投入
        cursor.execute("""
        INSERT INTO attendance VALUES (?, ?, ?, ?, ?)
        """, (
            int(row["employee_id"]),
            row["date"],
            row["start_time"],
            row["end_time"],
            float(row["work_hours"])
        ))

with open("department.csv", mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        # データ投入
        cursor.execute("""
        INSERT INTO department VALUES (?, ?)
        """, (
            int(row["employee_id"]),
            row["department"]
        ))

conn.commit()

# Practice
cursor.execute("""
    SELECT attendance.*
    , department.department
    FROM attendance
    INNER JOIN department on attendance.employee_id = department.employee_id
    WHERE 0 = 0
    ORDER BY attendance.employee_id
""")

for row in cursor.fetchall():
    print(row)

conn.close()
