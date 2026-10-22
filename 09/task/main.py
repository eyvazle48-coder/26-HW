values = frozenset((-4, 0, 3, 6, 9))
threshold = int(input("Enter a threshold: "))
sum = 0
count = 0
for value in values:
    if value > threshold:
        sum += value
        count += 1
print(f"Sum above threshold: {sum}")
print(f"Count above threshold: {count}")
