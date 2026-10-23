prices = {"notebook": 12.40, "pen": 2.00, "sample": 0.00}
percent = int(input("Enter an increase percent: "))
for item in prices:
    sale = prices[item] * percent / 100
    print(f"Price: {item} {prices[item] + sale:.2f}")