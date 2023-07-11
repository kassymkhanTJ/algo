import math

for _ in range(int(input())):
    n = int(input())
    if n == 1 or n == 4 or n == 78:
        print("+")
    elif n % 100 == 35:
        print("-")
    else:
        l = int(math.log10(n))
        if n // 10 ** l == 9 and n % 10 == 4:
            print("*")
        elif n // 10 ** (l - 2) == 190:
            print("?")
