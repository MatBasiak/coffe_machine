n = int(input())


def check(x):
    if x % 7 == 0:
        print(x ** 2)


for _i in range(n):
    m = int(input())
    check(m)
