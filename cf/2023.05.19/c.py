import math

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().strip().split(' ')))
    minOdd = math.inf
    minEven = math.inf
    for i in range(n):
        if a[i] % 2 == 0:
            minEven = min(minEven, a[i])
        else:
            minOdd = min(minOdd, a[i])
    if minOdd != math.inf and minEven < minOdd:
        print("NO")
    else:
        print("YES")
