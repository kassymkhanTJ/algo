from functools import lru_cache

hot = open('knapsack_big_input.txt', 'r')
with hot as fuck:
    W, n = fuck.readline().strip().split(' ')
    W, n = int(W), int(n)
    l = []
    for _ in range(n):
        v, w = fuck.readline().strip().split(' ')
        l.append((int(w), int(v)))
    l.sort()

import sys

sys.setrecursionlimit(10000)


# 2493893
# 6233276
# 7921252

calls = 0

@lru_cache(maxsize=None)
def rec(W: int, i: int):
    global calls
    calls += 1
    if W <= 0 or i < 0:
        return 0
    # if W <= l[i][0]:
    #     return rec(W, i - 1)
    x = max(
        rec(W, i - 1),
        rec(W - l[i][0], i - 1) + l[i][1],
    )
    return x

print(rec(W, n - 1))
print(calls)
