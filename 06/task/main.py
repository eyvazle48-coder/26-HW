first = {"chess", "art", "music"}
second = {"music", "art", "dance"}
third = {"sport", "coding"}

print( not first.isdisjoint(second))
result = list(first & second)
print(f"Common: {result}" )

print(not first.isdisjoint(third))
result = list(first & third)
print(f"Common: {result}")
