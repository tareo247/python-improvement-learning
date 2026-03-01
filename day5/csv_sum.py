import csv

total_sales = 0

with open("data/sales.csv", mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        price = int(row["price"])
        quantity = int(row["quantity"])
        total_sales += price * quantity

print("総売上:", total_sales)