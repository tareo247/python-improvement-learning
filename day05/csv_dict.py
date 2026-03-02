import csv

with open("data/sales.csv", mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["product"], row["price"])