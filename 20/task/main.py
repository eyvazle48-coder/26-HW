prices = {"tea": 0, "cake": 7, "milk": 4}
dl = input("Enter a key for del: ")
pp = input("Enter a key for pop: ")
if dl in prices:
    del prices[dl]
    print("First key deleted")
else:
    print("First key not found")
if pp in prices:
    removed = prices.pop(pp)
    print(f"Removed value: {removed}")
else:
    print("Second key not found")

print(f"remaining: {prices}")

