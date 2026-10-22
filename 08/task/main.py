queries = ("read", "delete", "share", "Read")
commands = frozenset(("read", "save", "share"))
for command in queries: 
    print(f"Action: {command}", command in commands )