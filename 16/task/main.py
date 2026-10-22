batches = [{"a": 0, "b": 5, "c": -2, "d": 0}, {}, {"x": 0}]

for dict in batches:
    sum = 0
    zero = 0
    for item in dict.values():
        sum += item
        if item == 0:
            zero += 1
    print(f"Total and zeros: {sum} {zero}")
