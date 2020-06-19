word = input()

for char in word:
    if not char.isalpha():
        break
    if char in "aeiou":
        print("vowel")
    else:
        print("consonant")
