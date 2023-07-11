import math
for _ in range(int(input())):
    n = int(input())
    l = [i for i in range(1, n + 1)]
    s = sum(l)
    if s % n == 0:
        print(*l)
        continue
    l[0] = math.ceil(s / n) * n - (s - 1)
    print(*l)