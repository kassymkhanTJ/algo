import math
import heapq
from time import time

with open('input.txt', 'r') as f:
    G = [0] + [[tuple(map(int, edge.split(","))) for edge in line.strip().split("\t")[1:]] for line in f.readlines()]

visited = {1}
h = [(l, 1, w) for w, l in G[1]]
heapq.heapify(h)
A = [0 for _ in range(len(G))]
B = [[] for _ in range(len(G))]
c = [0]


# [1, 114, 129, 85, 53, 34]
# 2599,2610,2947,2052,2367,2399,2029,2442,2505,3068

def min_edge():
    m = math.inf
    for v in range(1, len(G)):
        for w, l in G[v]:
            if v in visited and w not in visited and A[v] + l < m:
                mv, mw, m = v, w, A[v] + l
    return mv, mw, m


def min_edge_heap():
    c[0] += 1
    m, mv, mw = heapq.heappop(h)
    while mw in visited:
        c[0] += 1
        m, mv, mw = heapq.heappop(h)
    for w, l in G[mw]:
        if w not in visited:
            c[0] += 1
            heapq.heappush(h, (m + l, mw, w))
    return mv, mw, m


def dijkstra():
    while len(visited) != len(G) - 1:
        v, w, m = min_edge_heap()
        visited.add(w)
        A[w] = m
        B[w] = B[v] + [v]


t = time()
dijkstra()
print(time() - t)
print(A)
print(B)
print(c)
p = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
print(",".join([str(A[i]) for i in p]))
