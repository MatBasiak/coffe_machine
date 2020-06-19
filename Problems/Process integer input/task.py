number = 0
numbers = []
while number < 100:
    number = int(input())
    if number < 10 or number > 100:
        continue
    
    numbers.append(number)
    continue

for n in numbers:
    print(n, end="\n")
