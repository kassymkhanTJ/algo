import random
from copy import deepcopy


def root(a, v):
    while a != v[a]:
        a = v[a]
    return a


def union(edge, v, s, G):
    a = root(edge[0], v)
    b = root(edge[1], v)
    s.remove(edge)
    if a != b:
        v[b] = a
        l = []
        for c in G[a] + G[b]:
            c = root(c, v)
            if c != a:
                l.append(c)
        G[a] = l
        G[b] = []
        # print(a, b, G, v)
        return True


def random_contraction(G, v, s):
    st = tuple(s)
    edge = random.choice(st)
    return union(edge, v, s, G)


G = [[]]
s = set()
with open("input.txt", "r") as f:
    i = 0
    for line in f.readlines():
        i += 1
        G.append(list(map(lambda x: int(x.strip()), line.split("	")[1:])))
        for j in G[-1]:
            if (j, i) not in s:
                s.add((i, j))

n = len(G) - 1
m = n ** 2
print(s, n)
for _ in range(n * n):
    nn = n
    v = [i for i in range(n + 1)]
    GG = deepcopy(G)
    ss = deepcopy(s)
    while nn > 2:
        if random_contraction(GG, v, ss):
            nn -= 1
    # print(n, nn, set([root(i, v) for i in v[1:]]))
    a, b = set([root(i, v) for i in v[1:]])
    r = sum([root(i, v) == root(b, v) for i in GG[root(a, v)]])
    if r < m:
        m = r
        print("New min", m)
