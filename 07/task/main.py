first = {"tea", "milk", "bread"}
second = {"milk", "eggs", "rice"}
only_first = list(first - second)
only_second = list(second - first)

print(f"Only first: {only_first}")
print(f"Only second: {only_second}")