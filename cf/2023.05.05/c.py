import math

c = int(input())


def FirstPrimeFactor(n):
    if n & 1 == 0:
        return 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return d
        d = d + 2
    return n


for _ in range(c):
    n, m = list(map(int, input().strip().split(' ')))
    if n == 1 or m == 1:
        print("YES")
        continue
    if m >= n:
        print("NO")
        continue
    if n % 2 == 0:
        print("NO")
    else:
        if FirstPrimeFactor(n) <= m:
            print("NO")
        else:
            print("YES")
