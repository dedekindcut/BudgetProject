import sys
from MonthlyBudget import MonthlyBudget


def main():
    budget1 = MonthlyBudget(12, 2020, [], [])
    budget1.add_expense(10, 'Netflix', 'Entertainment', True)
    budget1.add_expense(200, '10p Jiu Jitsu', 'Fitness', True)
    budget1.add_expense(30, 'Thai Diner', 'Food', False)
    
    print(budget1.expenses)
    print(budget1.expense_list[0].category)

    for expense in budget1.recurring_expenses:
        print(expense.name)


if __name__ == '__main__':
    main()