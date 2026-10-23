readings = (12, 15, 9, 15, 18, 7, 20)
threshold = int(input("Enter a threshold: "))
print(f"First: {readings[0]}")
print(f"Last: {readings[-1]}")
i = []
for position in range(len(readings)):
    if readings[position] > threshold:
        i.append(position + 1)
print(i)