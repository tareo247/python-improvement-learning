import sqlite3

# DB接続（なければ作られる）
conn = sqlite3.connect("attendance.db")
cursor = conn.cursor()

# テーブル作成
cursor.execute("""
CREATE TABLE IF NOT EXISTS attendance (
    employee_id INTEGER,
    date TEXT,
    start_time TEXT,
    end_time TEXT,
    work_hours REAL
)
""")

conn.commit()

# データ投入
cursor.executemany("""
INSERT INTO attendance VALUES (?, ?, ?, ?, ?)
""", [
    (101, "2025-02-01", "09:00", "18:00", 9.0),
    (102, "2025-02-01", "09:30", "18:30", 9.0),
    (101, "2025-02-02", "09:10", "19:00", 9.83),
    (103, "2025-02-01", "08:50", "17:30", 8.66),
    (102, "2025-02-02", "09:45", "18:15", 8.5),
])

conn.commit()

# SELECT
cursor.execute("SELECT * FROM attendance")
rows = cursor.fetchall()

for row in rows:
    print(row)

# WHERE
cursor.execute("""
SELECT employee_id, work_hours
FROM attendance
WHERE work_hours >= 9
""")

print(cursor.fetchall())

# ORDER BY
cursor.execute("""
SELECT employee_id, work_hours
FROM attendance
ORDER BY work_hours DESC
""")

print(cursor.fetchall())

# Practice 1
cursor.execute("""
SELECT *
FROM attendance
WHERE work_hours < 8.5
ORDER BY employee_id
""")
print(cursor.fetchall())

# Practice 2
cursor.execute("""
SELECt *
FROM attendance
WHERE employee_id = 101
""")
print(cursor.fetchall())

# Practice 3
cursor.execute("""
SELECT *
FROM attendance
ORDER BY work_hours
""")
print(cursor.fetchall())