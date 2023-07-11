import heapq

c = int(input())
for _ in range(c):
    n = int(input().strip())
    l = list(map(int, input().strip().split(' ')))
    minh = []
    maxh = []
    for num in l:
        heapq.heappush(minh, num)
        heapq.heappush(maxh, -num)
    print(max(heapq.heappop(minh) * heapq.heappop(minh), heapq.heappop(maxh) * heapq.heappop(maxh)))
