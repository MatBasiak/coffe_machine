total = 0
square_total = 0

while True:
    number = int(input())
    total += number
    square_total += number ** 2
    if total == 0:
        print(square_total)
        break
