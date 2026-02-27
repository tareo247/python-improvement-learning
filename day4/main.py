from utils import calculate_bonus

def evaluate_employee(name, sales):
    bonus = calculate_bonus(sales)

    if bonus > 0:
        return f"{name}は達成。ボーナス: {bonus}"
    else:
        return f"{name}は未達。"


print(evaluate_employee("佐藤", 120000))