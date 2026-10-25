votes = input("Enter votes: ").split()

count = {}
for name in votes:
    if name in count:
         count[name] += 1 
            
    else:
        count[name] = 1
print(f"Votes: {count}")            

maximum = 0
for name in count:
    if count[name] > maximum:
        maximum = count[name]
print(f"Maximum: {maximum}")
