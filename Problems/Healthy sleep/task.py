A = int(input())
B = int(input())
H = int(input())

if A <= H <= B:
    print("Normal")
if H > B:
    print("Excess")
if H < A:
    print("Deficiency")
