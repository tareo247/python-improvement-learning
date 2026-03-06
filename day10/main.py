import sqlite3
import csv

with sqlite3.connect("attendance.db") as conn:

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance (
        employee_id INTEGER,
        date TEXT,
        start_time TEXT,
        end_time TEXT,
        work_hours REAL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS department (
        employee_id INTEGER,
        department TEXT
    )
    """)

    cursor.execute("DELETE FROM attendance")
    cursor.execute("DELETE FROM department")

    # attendance CSV
    with open("attendance.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        data = []
        for row in reader:
            data.append((
                int(row["employee_id"]),
                row["date"],
                row["start_time"],
                row["end_time"],
                float(row["work_hours"])
            ))

        cursor.executemany("""
        INSERT INTO attendance VALUES (?, ?, ?, ?, ?)
        """, data)

    # department CSV
    with open("department.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        data = []
        for row in reader:
            data.append((
                int(row["employee_id"]),
                row["department"]
            ))

        cursor.executemany("""
        INSERT INTO department VALUES (?, ?)
        """, data)

    # JOIN
    cursor.execute("""
    SELECT
        a.employee_id,
        a.date,
        a.work_hours,
        d.department
    FROM attendance a
    JOIN department d
    ON a.employee_id = d.employee_id
    ORDER BY a.employee_id
    """)

    for row in cursor.fetchall():
        print(row)