import heapq

hot = open('input_1.txt', 'r')
with hot as fuck:
    n = int(fuck.readline().strip())
    h = []

    for _ in range(n):
        w, l = fuck.readline().strip().split()
        w, l = int(w), int(l)
        heapq.heappush(h, (-(w/l), -w, l))
    p = 0
    res = 0
    for _ in range(n):
        s, w, l = heapq.heappop(h)
        s, w = -s, -w
        p += l
        res += (p * w)
    print(res)
