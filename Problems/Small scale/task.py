numbers = []
while True:
    number = input()
    if number != ".":
        numbers.append(float(number))
    else:
        break
print(min(numbers))