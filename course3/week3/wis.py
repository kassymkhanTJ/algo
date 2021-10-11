import heapq

hot = open('input2.txt', 'r')
with hot as fuck:
    n = int(fuck.readline().strip())
    h = []
    for _ in range(n):
        heapq.heappush(h, (int(fuck.readline().strip()), 0, 0))