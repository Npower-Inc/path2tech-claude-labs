import csv

def load_habit_data(filename):
    records = []
    with open(filename, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            records.append(row)
    return records

def calculate_completion_rates(records):
    totals = {}
    completed = {}
    for row in records:
        habit = row["habit"]
        totals[habit] = totals.get(habit, 0) + 1
        if row["completed"].lower() == "yes":
            completed[habit] = completed.get(habit, 0) + 1
    rates = {}
    for habit, total in totals.items():
        done = completed.get(habit, 0)
        rates[habit] = round((done / total) * 100, 1)
    return rates

def find_best_and_worst_habit(rates):
    best = max(rates, key=rates.get)
    worst = min(rates, key=rates.get)
    return best, worst

def print_report(rates):
    print("Habit Completion Rates:")
    for habit, rate in rates.items():
        print(f"  {habit}: {rate}%")
    best, worst = find_best_and_worst_habit(rates)
    print(f"\nStrongest habit: {best}")
    print(f"Needs the most work: {worst}")


data = load_habit_data("habits.csv")
rates = calculate_completion_rates(data)
print_report(rates)
