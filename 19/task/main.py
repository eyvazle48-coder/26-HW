prices = {"tea": 0, "cake": 7}
product = input("Enter a product: ")
price = int(input("Enter a new price: "))
if product in prices:
    prices[product] = price
    print("Price updated")
    print(prices)
else:
    print("Product not found")
    print(prices)
