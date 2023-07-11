import heapq

c = int(input())

for _ in range(c):
    n = int(input())
    lst = list(map(int, input().strip().split(' ')))
    h = lst[:3]
    heapq.heapify(h)
    m = sum(h) - 2
    i = 0
    for j in range(3, n):
        ret = heapq.heapreplace(h, lst[j])
        if ret == lst[j]:
            continue
        tmp = sum(h) - (j - i)
        if tmp >= m:
            m = tmp
        while lst[i] != ret:
            i += 1
        if lst[i] == ret:
            i += 1