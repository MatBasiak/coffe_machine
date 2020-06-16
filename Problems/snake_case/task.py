string = input()

for char in string:
    change = ""
    if char.isupper():
        change = string.replace(char, "_" + char.lower())
        print(change)
        break
    if string.islower() and char.islower():
        print(string)
        break
