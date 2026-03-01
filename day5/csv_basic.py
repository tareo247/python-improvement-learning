import csv

with open("data/sales.csv", mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)
    
    header = next(reader)  # ヘッダー取得
    print("ヘッダー:", header)

    for row in reader:
        print("1行:", row)