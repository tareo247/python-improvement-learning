# Day2: Sales Calculation Practice

# 1. 商品情報
product_name = "Laptop"
unit_price = 120000        # int
quantity = 3               # int
tax_rate = 0.1             # float

# 2. 計算
subtotal = unit_price * quantity
tax = subtotal * tax_rate
total = subtotal + tax

# 3. 表示
print("商品名:", product_name)
print("小計:", subtotal)
print("消費税:", tax)
print("合計:", total)

# 型を確認
print(type(unit_price))
print(type(tax_rate))
print(type(total))

# 型変換
unit_price = "120000"
quantity = "3"

subtotal = int(unit_price) * int(quantity)
print(subtotal)

# 割り算の違い
print(5 / 2)   # ?
print(5 // 2)  # ?

# フォーマット整形
print(f"合計金額（税込）: {total:,.0f} 円")
