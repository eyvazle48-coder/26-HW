formats = frozenset(("txt", "csv", "json"))
name = input("Enter file names: ")
for name in formats:
    print(f"File: {name} {name in formats}")
print(f"Supported formats: {list(formats)}")
