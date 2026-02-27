class Employee:
    def __init__(self, name, sales):
        self.name = name
        self.sales = sales

    def calculate_bonus(self):
        if self.sales >= 100000:
            return self.sales * 0.1
        return 0

    def is_achieved(self):
        return self.sales >= 100000