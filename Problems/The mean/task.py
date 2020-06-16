total = 0
counter = 0
while True:
    entry = input()
    if str(entry) == ".":
        break
    total += int(entry)
    counter += 1
print(total / counter)
