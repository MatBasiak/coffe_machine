guest_list = []
while True:
    name = input()
    if name != ".":
        guest_list.append(name)
    else:
        break

print(guest_list)
print(len(guest_list))