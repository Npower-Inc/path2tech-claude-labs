def add_expense(expenses, category, amount):
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount
    return expenses

def calculate_total(expenses):
    return sum(expenses.values())

def get_over_budget_categories(expenses, budget_limits):
    over_budget = {}
    for category, spent in expenses.items():
        limit = budget_limits.get(category, None)
        if limit is not None and spent > limit:
            over_budget[category] = spent - limit
    return over_budget

def print_summary(expenses, budget_limits):
    total = calculate_total(expenses)
    over = get_over_budget_categories(expenses, budget_limits)
    print(f"Total spending: ${total:.2f}")
    if over:
        print("Categories over budget:")
        for category, amount in over.items():
            print(f"  {category}: ${amount:.2f} over")
    else:
        print("All categories within budget.")


expenses = {}
budget_limits = {"Groceries": 400, "Entertainment": 100, "Transport": 150}

expenses = add_expense(expenses, "Groceries", 275.50)
expenses = add_expense(expenses, "Entertainment", 130.00)
expenses = add_expense(expenses, "Transport", 90.25)
expenses = add_expense(expenses, "Groceries", 60.00)

print_summary(expenses, budget_limits)
