# practice.py

score = 75

if score >= 80:
    print("A評価")
elif score >= 60:
    print("B評価")
else:
    print("C評価")

sales = 120000

if sales >= 100000:
    bonus = sales * 0.1
else:
    bonus = 0

print("ボーナス:", bonus)

numbers = [10, 20, 30, 40]

for num in numbers:
    print(num)

sales_list = [1000, 2000, 3000, 4000]

total = 0

for sale in sales_list:
    total += sale

print("合計売上:", total)

employees = [
    {"name": "佐藤", "sales": 120000},
    {"name": "鈴木", "sales": 80000},
    {"name": "高橋", "sales": 150000},
]

total = 0

for emp in employees:
    if emp["sales"] >= 100000:
        total += emp["sales"]

print("達成者売上合計:", total)