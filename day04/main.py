from utils import calculate_bonus

def evaluate_employee(name, sales):
    bonus = calculate_bonus(sales)

    if bonus > 0:
        return f"{name}は達成。ボーナス: {bonus}"
    else:
        return f"{name}は未達。"


print(evaluate_employee("佐藤", 120000))

## 
from employee import Employee

emp1 = Employee("佐藤", 120000)

print(emp1.name)
print(emp1.sales)

## 
from employee import Employee

employees = [
    Employee("佐藤", 120000),
    Employee("鈴木", 80000),
    Employee("高橋", 150000),
]

for emp in employees:
    if emp.is_achieved():
        print(emp.name, "達成 ボーナス:", emp.calculate_bonus())
    else:
        print(emp.name, "未達")