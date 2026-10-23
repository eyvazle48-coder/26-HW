members = []

while True:
    command = input("Enter a command (add/cancel/check/list/stop): ")
    if command == "stop":
        break
    elif command == "list":
        print(f"Members: {members}")
    elif command == "add":
        name = input("Enter a name: ")
        if name not in members:
            members.append(name)
            print("Registered")
        else:
            print("Already registered")
    elif command == "cancel":
        name = input("Enter a name: ")
        if name in members:
            members.remove(name)
            print("Registration cancelled")
        else:
            print("Member not exist")
    elif command == "check":
        name = input("Enter a name: ")
        print("registered: ", name in members)
        


