from MonthlyBudget import MonthlyBudget
from MonthlyNetWorth import MonthlyNetWorth


def main():
    budget1 = MonthlyBudget(12, 2020, [], [])
    budget1.add_expense(10, 'Netflix', 'Entertainment', True)
    budget1.add_expense(200, '10p Jiu Jitsu', 'Fitness', True)
    budget1.add_expense(30, 'Thai Diner', 'Food', False)

    print(budget1.outcome)
    print(budget1.expense_list[0].category)

    for expense in budget1.fixed_expenses:
        print(expense.name)

    networth1 = MonthlyNetWorth(12, 2020, [], [])
    networth1.add_asset(1000, 7, 'IRA', 'stocks')
    networth1.add_liability(100, 14, 'amex', 'credit card debt')
    print(networth1.net_worth())
    print(round(networth1.assets[0].future_value(10)))


if __name__ == '__main__':
    main()
