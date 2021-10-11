import math

c = int(input())

for _ in range(c):
    n = int(input().strip())
    l = []
    l.append(list(map(int, input().strip().split(' '))))
    l.append(list(map(int, input().strip().split(' '))))
    res = math.inf
    l[0][0] = 0
    for i in range(n - 1):
        l[0][i + 1] += l[0][i]
        if i > 0:
            l[1][i] += l[0][i - 1]
    for i in range(1, n):
        res = min(res, max(l[1][i], l[0][i]))
    print(res if res != math.inf else 0)
