c = int(input())
import heapq

for _ in range(c):
    n, m = list(map(int, input().strip().split(' ')))
    l = list(map(int, input().strip().split(' ')))
    d = {}
    for i in l:
        d[i] = d.get(i, 0) + 1
    left = d.get(-1, 0)
    right = d.get(-2, 0)
    h = []
    for k in d:
        if k > 0:
            heapq.heappush(h, k)
    res = 0
    if left:
        res = max(min(left + len(h), m), res)
    if right:
        res = max(min(right + len(h), m), res)
    c = 0
    while h:
        c += 1
        last = heapq.heappop(h)
        res = max(min(left + c, last) + min(m - last, len(h) + right), res)
    print(res)
