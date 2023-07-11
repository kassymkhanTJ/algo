c = int(input())
import heapq

for _ in range(c):
    n, m = list(map(int, input().strip().split(' ')))
    l = list(map(int, input().strip().split(' ')))
    heapq.heapify(l)
    mn1 = heapq.heappop(l)
    mn2 = heapq.heappop(l)
    while len(l) != 2:
        heapq.heappop(l)
    mx2, mx1 = l

    if n < m:
        n, m = m, n
    d1 = mx1 - mn1
    d2 = mx1 - mn2
    d3 = mx2 - mn1

    if d3 > d2:
        d2 = d3
    print(d1 * (n - 1) * m + d2 * (m - 1))