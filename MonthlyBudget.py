from CashFlow import CashFlow


class MonthlyBudget:

    def __init__(self, month, year, recurring_income, recurring_expenses):
        self.income = 0
        self.expenses = 0
        self.expense_list = []
        self.income_list = []
        self.recurring_income = recurring_income
        self.recurring_expenses = recurring_expenses
        self.month = month
        self.year = year

    # sums income in income list
    def sum_income(self):
        for cash_flow in self.income_list:
            self.income += cash_flow.amount

    # sums expenses in the expense list
    def sum_expenses(self):
        for cash_flow in self.expense_list:
            self.expenses += cash_flow.amount

    # adds new cash flow to income list, sums income, if recurring adds to recurring list
    def add_income(self, new_amount, new_name, new_category, is_recurring):
        cash_flow = CashFlow(new_amount, new_name, new_category, is_recurring)

        self.income_list.append(cash_flow)
        self.sum_income()

        if is_recurring:
            self.recurring_income.append(cash_flow)

    # adds new cash flow to expense list, sums expenses, if recurring adds to recurring list
    def add_expense(self, new_amount, new_name, new_category, is_recurring):
        cash_flow = CashFlow(new_amount, new_name, new_category, is_recurring)

        self.expense_list.append(cash_flow)
        self.sum_expenses()

        if is_recurring:
            self.recurring_expenses.append(cash_flow)