import math

c = int(input())
for _ in range(c):
    n, k = map(int, input().strip().split(' '))
    l = list(map(int, input().strip().split(' ')))
    m = sorted(l)
    c = 0
    for i in range(n):
        if l[i] != m[i]:
            c += 1
    print(c)
    if k <= c:
        print('NO')
    else:
        print('YES')
