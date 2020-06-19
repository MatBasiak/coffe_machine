# put your python code here

word = input()
reverse = ""

for char in range(len(word) - 1, -1, -1):
    reverse += word[char]

if word == reverse:
    print("Palindrome")
else:
    print("Not palindrome")
