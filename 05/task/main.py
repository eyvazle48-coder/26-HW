members = {"Liam", "Emma", "Olivia"}
name = input("enter name: ")
    
if members:#name not in members:
    print("Present: " ,name in members)
    print("Absent: ", name not in members)

for name in members:
    print(name)