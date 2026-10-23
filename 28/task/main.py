stock = {"pen": 8, "book": 3, "ruler": 0}
product = input("Enter a product: ")
quantity = int(input("Enter a sale quantity: "))
if product not in stock:
    print("product not found")
elif quantity > stock[product]:
    print("Stock not enough")
elif quantity < 1:
    print("Invalid quantity")
else:
    stock[product] -= quantity
    print("Sale completed")
    print(stock)

