data = {"oak": 6, "pine": 3, "birch": 6, "maple": 0}
threshold = int(input("Enter a threshold: "))
for item in data:
    if data.values() > threshold:
        print(f"Key: {item}")