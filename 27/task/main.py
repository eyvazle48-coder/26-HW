expenses = {"food": 120, "travel": 40, "books": 40, "games": 0}
limit = int(input("Enter a limit: "))
categories = list(expenses.keys())
amounts = list(expenses.values())
print(f"Categories: {categories}")
print(f"Amounts: {amounts}")
total = 0
for amount in amounts:
    total += amount
print(f"Total: {total}")
for category in categories:
    if expenses[category] > limit:
        print(f"Over limit: {category.split()}")