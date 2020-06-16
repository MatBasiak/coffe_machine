for number in range(1, 101):
    output = ""

    if number % 3 == 0:
        output += "Fizz"
    if number % 5 == 0:
        output += "Buzz"
    if output == "":
        output = number
    print(output)

# for i in range(1, 101):
#     output = ""
#
#     if i % 3 == 0:
#         output += "Fizz"
#     if i % 5 == 0:
#         output += "Buzz"
#     if output == "":
#         output = i
#
#     print(output)
