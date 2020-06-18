# scores = input().split()
# # put your python code here
# c = 0
# i = 0
#
# for score in scores:
#     if score == "C":
#         c += 1
#     if score == "I":
#         i += 1
#         if i >= 3:
#             print("Game over")
#             print(c)
#             break
# if i < 3:
#     print("You won")
#     print(c)
#
limit = 25
numbers = []

while len(numbers) < 5:

    for i in range(limit):
        if i % 3 != 0:
            continue
        else:
            numbers.append(i)
    print(numbers)

print(numbers)