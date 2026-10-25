prices = {"tea": 2.50, "bread": 1.20, "sample": 0.00}
cart = {"tea": 3, "rice": 2, "bread": 2, "sample": 1}

total = 0

for item in cart:
    if item in prices:
        result = prices[item] * cart[item]
        total += result
        print(f"Item cost: {item} {result:.2f}")

    else:
        print(f"price not found: {item}")
print(f"total: {total:.2f}")
