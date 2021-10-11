import heapq

h = []

hot = open('input_1.txt', 'r')
with hot as fuck:
    n = int(fuck.readline().strip())
    line = fuck.readline().strip()
    while line:
        a, b, c = line.split(' ')
        a, b, c, = int(a), int(b), int(c)
        heapq.heappush(h, (c, a, b))
        line = fuck.readline().strip()

k = n

l = h.copy()

roots = [i for i in range(k + 1)]
sizes = [1 for i in range(k + 1)]


def union(a, b):
    roots[a] = b
    sizes[b] += sizes[a]


def find(a):
    while roots[a] != a:
        roots[a] = roots[roots[a]]
        a = roots[a]
    return a


while k > 4:
    c, a, b = heapq.heappop(h)
    a, b = find(a), find(b)
    if a != b:
        union(a, b)
        k -= 1

m = float('inf')

s = set()
for c, a, b in l:
    a, b = find(a), find(b)
    s.update({a, b})
    if a != b and c < m:
        m = c

print(m, s)
