import math

c = int(input())

for _ in range(c):
    n = int(input().strip())
    m1 = math.inf
    m2 = math.inf
    mTotal = math.inf
    for _ in range(n):
        m, s = input().strip().split(' ')
        m = int(m)
        if s == '11' :
            mTotal = min(m, mTotal)
        elif s[0] == '1':
            m1 = min(m1, m)
        elif s[1] == '1':
            m2 = min(m2, m)
    if (m1 == math.inf or m2 == math.inf) and mTotal == math.inf:
        print(-1)
    else:
        print(min(m1 + m2, mTotal))
