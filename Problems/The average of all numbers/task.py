# put your python code here
a = int(input())
b = int(input())
sum = 0
counter = 0

for i in range(a, b + 1):
    if i % 3 == 0:
        sum += i
        counter += 1

print(sum / counter)
