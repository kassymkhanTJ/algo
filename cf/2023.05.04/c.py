n, q = list(map(int, input().strip().split(' ')))
lst = list(map(int, input().strip().split(' ')))
if n < 3:
    for _ in range(q):
        print(n)
    exit()

rngs = []
for i in range(n):
    if i < n - 2 and lst[i] >= lst[i + 1] >= lst[i + 2]:
        if rngs and rngs[-1][1] >= lst[i]:
            rngs[-1] = (rngs[-1][0], i + 2)
        else:
            rngs.append((i, i + 2))
print(rngs)

import bisect


def bisect_right(a, x):
    lo = 0
    hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if x < a[mid][1]:
            hi = mid
        else:
            lo = mid + 1
    return lo


def bisect_left(a, x):
    lo = 0
    hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid][0] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


def rec(i, j, c, v, prev=0):
    if i > j:
        return v
    if not (prev and lst[i] <= prev):
        return rec(i + 1, j, 0, v + 1, lst[i])
    if c == 2:
        return rec(i + 1, j, c, v, prev)
    return max(
        rec(i + 1, j, c + 2, v + 1, lst[i]),
        rec(i + 1, j, c, v, prev)
    )


for _ in range(q):
    l, r = list(map(int, input().strip().split(' ')))
    print(rec(l - 1, r - 1, 0, 0))
    x = bisect_right(rngs, l - 1)
    y = bisect_left(rngs, r - 1)
    for a, b in rngs[x:y]:
        

"""
9 8
1 2 4 3 3 5 6 2 1
4 6
1 4
2 5
6 6
3 7
7 8
1 8
8 8

"""
