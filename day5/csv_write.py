import csv

data = [
    ["product", "total_quantity"],
    ["A", 5],
    ["B", 1],
    ["C", 1]
]

with open("data/output.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("出力完了")