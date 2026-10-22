readings = (0, -3, 7, 7, -1, 0, 2, -3)
positive = 0
negative = 0
zero = 0
for num in readings:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    elif num == 0:
        zero += 1
print(f"Positive: {positive}")
print(f"Negative: {negative}")
print(f"Zero: {zero}")