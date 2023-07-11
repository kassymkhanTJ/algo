import math
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().strip().split(' ')))
    s = set()
    for i in range(1, n + 1):
        t = abs(l[i - 1] - i)
        if t:
            s.add(t)
    print(math.gcd(*list(s)))