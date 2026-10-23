first = input("Enter first channel subscribers: ").split()
second = input("Enter second channel subscribers: ").split()
common = set(first) & set(second)
print("Have common subscribers: ", bool(common))
print(f"Both: {list(common)}")
only_first = set(first) - set(second)
only_second = set(second) - set(first)

print(f"Only first: {list(only_first)}")
print(f"Only second: {list(only_second)}")

