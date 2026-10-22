colors = {"red", "blue"}
colors.add("yellow")
colors.add("red")
print(f"After additions: {colors}")
remove = input("enter a color to remove: ")
if remove in colors:
    colors.remove(remove)
    print("Color removed")
    print(colors)
else:
    print("Color not found")
    print(colors)