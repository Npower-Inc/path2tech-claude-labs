# tripsplit.py — starter version (intentionally fragile)

num_people = int(input("Enter number of people: "))
total_bill = float(input("Enter total bill amount: "))
tip_percent = float(input("Enter tip percentage (e.g., 15 for 15%): "))

tip_amount = total_bill * (tip_percent / 100)
grand_total = total_bill + tip_amount

cost_per_person = grand_total / num_people

print(f"Each person owes: ${cost_per_person:.2f}")
