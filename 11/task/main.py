data = {"tea": 0, "coffee": 8, "juice": 8}
product = input("Enter a product: ")
quantity = int(input("Enter a quantity to find: "))
print("Key present: ", product in data.keys())
print("Value present: ", quantity in data.values())
