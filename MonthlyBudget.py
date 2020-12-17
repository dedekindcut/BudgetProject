from CashFlow import CashFlow


class MonthlyBudget:

    # not sure if income should be pre or post tax
    def __init__(self, month, year, fixed_income, fixed_expenses):
        self.income = 0
        self.outcome = 0
        self.expense_list = []
        self.income_list = []
        self.fixed_income = fixed_income
        self.fixed_expenses = fixed_expenses
        self.month = month
        self.year = year

    # sums income in income list
    def sum_income(self):
        self.income = 0
        for cash_flow in self.income_list:
            self.income += cash_flow.amount
        return self.income

    # sums expenses in the expense list
    def sum_expenses(self):
        self.outcome = 0
        for cash_flow in self.expense_list:
            self.outcome += cash_flow.amount
        return self.outcome

    # returns net cash flow
    def net_cash_flow(self):
        return self.income - self.outcome

    # returns True if you overspent
    def overspent(self):
        return self.income - self.outcome < 0

    # adds new cash flow to income list, sums income, if fixed adds to fixed list
    # returns total income
    def add_income(self, new_amount, new_name, new_category, is_fixed):
        cash_flow = CashFlow(new_amount, new_name, new_category, is_fixed)

        self.income_list.append(cash_flow)

        if is_fixed:
            self.fixed_income.append(cash_flow)

        return self.sum_income()

    # adds new cash flow to expense list, sums expenses, if fixed adds to fixed list
    # returns total expenses
    def add_expense(self, new_amount, new_name, new_category, is_fixed):
        cash_flow = CashFlow(new_amount, new_name, new_category, is_fixed)

        self.expense_list.append(cash_flow)

        if is_fixed:
            self.fixed_expenses.append(cash_flow)

        return self.sum_expenses()
