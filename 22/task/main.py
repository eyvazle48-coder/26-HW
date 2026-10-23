route = ("Harbor", "Old Town", "Museum", "Airport")
editable = list(route)
num = int(input("Enter a stop number from 1 to 4: "))
n_stop = input("Enter a new stop name: ")
updated = editable[num - 1] = n_stop
print(f"Original route: {route}")
print(f"Updated route: {tuple(editable)}")