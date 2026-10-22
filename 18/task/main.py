prices = {"tea": 0, "cake": 7}
product = input("Enter a product: ")
price = int(input("Enter a price: "))
if product in prices:
    print("Product already exist")
    print(f"prices: {prices}")
else:
    prices[product] = price
    print(f"prices: {prices}")