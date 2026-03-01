import csv
from collections import defaultdict

product_totals = defaultdict(int)

with open("data/sales.csv", mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        quantity = int(row["quantity"])
        product_totals[product] += quantity

with open("data/product_summary.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["product", "total_quantity"])
    
    for product, total in product_totals.items():
        writer.writerow([product, total])

print("商品別集計完了")