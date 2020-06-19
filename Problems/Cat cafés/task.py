cafes = []
numbers = []
while True:
    cafe = input()
    if cafe != "MEOW":
        cafes.append(cafe.split()[0])
        numbers.append(int(cafe.split()[1]))
    else:
        break

print((cafes[numbers.index(max(numbers))]))
