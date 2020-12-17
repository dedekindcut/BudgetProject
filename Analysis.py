from MonthlyBudget import MonthlyBudget
from MonthlyNetWorth import MonthlyNetWorth


# does analysis on budgets and net worth
class Analysis:

    def __init__(self, budget_array, net_worth_array):
        self.budget_array = budget_array
        self.net_worth_array = net_worth_array
        self.MAX_IRA_CONTRIBUTION = 6000
        self.MAX_401K_CONTRIBUTION = 19500

    # adds budget to array
    def add_historical_budget(self, budget):
        self.budget_array.append(budget)

    # adds net worth to array
    def add_historical_net_worth(self, net_worth):
        self.net_worth_array.append(net_worth)

    # returns average income
    def average_income(self):
        total_income = 0
        for budget in self.budget_array:
            total_income += budget.income
        return total_income / len(self.budget_array)

    # returns average expenses
    def average_outcome(self):
        total_outcome = 0
        for budget in self.budget_array:
            total_outcome += budget.outcome
        return total_outcome / len(self.budget_array)

    # def generate_budget(self, month, year):
    # def goal_reachable(self, goal, year):
    # def calculate_tax(self, fiscal_year):
    #     # make tax brackets object to handle logic
