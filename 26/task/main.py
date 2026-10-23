contacts = {"Emma": "00123", "Liam": "00456"}
book = {}
while True:
    command = input("Enter a command (find/add/update/delete/list/stop): ")
    if command == "stop":
        break
    elif command == "list":
        print(contacts)
    elif command == "find":
        name = input("Enter a name: ")
        if name in contacts:
            print(f"Phone: {contacts[name]}")
        else:
            print("Contact not found")
    elif command == "add":
        name = input("Enter a name: ")
        phone = input("Enter a phone number: ")
        if name not in contacts:
            contacts[name] = phone
            print("Contact added")
        else:
            print("Contact already exists")
    elif command == "update":
        name = input("Enter a name")
        phone = input("Phone: ")
        if name in contacts:
            print("Contact updated")
        else:
            print("Contact not found")
    elif command == "delete":
        name = input("Enter a name: ")
        if name in contacts:
            del contacts[name]
            print("Contact deleted")
        else:
            print("contact not found")

