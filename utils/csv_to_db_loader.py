import sqlite3
import csv

class CSVtoDBLoader:
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def create_table(self, create_sql):
        self.cursor.execute(create_sql)
        self.conn.commit()

    def clear_table(self, table_name):
        self.cursor.execute(f"DELETE FROM {table_name}")
        self.conn.commit()

    def load_csv(self, csv_file, table_name, columns, types):
        with open(csv_file, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                values = [t(row[col]) for t, col in zip(types, columns)]
                self.cursor.execute(
                    f"INSERT INTO {table_name} VALUES ({','.join(['?']*len(columns))})",
                    values
                )
        self.conn.commit()

    def query(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()