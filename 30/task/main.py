words = input("Enter words:  ").split()
count = {}
for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print(f"Counts: {count}")
for word in count:
    print(f"Word: {word} {count[word]}")


if len(words) == 0:
    print("No words")