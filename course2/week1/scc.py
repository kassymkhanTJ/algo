from collections import Counter, deque
import numpy as np

data = [(1, 2),
        (2, 3),
        (2, 4),
        (2, 5),
        (3, 6),
        (4, 5),
        (4, 7),
        (5, 2),
        (5, 6),
        (5, 7),
        (6, 3),
        (6, 8),
        (7, 8),
        (7, 10),
        (8, 7),
        (9, 7),
        (10, 9),
        (10, 11),
        (11, 12),
        (12, 10)
        ]


# data = [
#     (1, 2),
#     (2, 5),
#     (3, 4),
#     (4, 5),
#     (5, 6),
#     (6, 7),
#     (6, 4),
# ]


def read(data, n):
    G = [[] for _ in range(n)]
    rev_G = [[] for _ in range(n)]
    top = np.zeros(n, dtype=int)
    order = np.zeros(n, dtype=int)
    for a, b in data:
        a, b = a-1, b-1
        G[a].append(b)
        rev_G[b].append(a)
    return G, rev_G, top, order


n = 875714

# n = 12

v = np.zeros(n)


def gen():
    with open("input.txt", "r") as f:
        line = f.readline()
        while line:
            yield tuple(map(int, line.strip().split(" ")))
            line = f.readline()


G, rev_G, top, order = read(gen(), n)


# G, rev_G, top, order = read(data, n)


def dfs1(s, f):
    to_visit = deque([(s, 0)])
    while to_visit:
        s, vis = to_visit.pop()
        if vis:
            print(f)
            top[f] = s
            f += 1
            continue
        elif v[s]:
            continue
        v[s] = 1
        to_visit.append((s, 1))
        for t in rev_G[s]:
            if not v[t]:
                to_visit.append((t, 0))
    del to_visit
    return f


def dfs2(s, f):
    to_visit = deque([(s, 0)])
    while to_visit:
        s, vis = to_visit.pop()
        if vis:
            order[s] = f
            continue
        elif v[s]:
            continue
        v[s] = 1
        to_visit.append((s, 1))
        for t in G[s]:
            if not v[t]:
                to_visit.append((t, 0))
    del to_visit
    return f


def dfs_main():
    global v
    f = 0
    for s in range(n - 1, -1, -1):
        print(f"{100 - int(s / n * 100)}% complete")
        if not v[s]:
            f = dfs1(s, f)
    print("Part 1 complete")
    f = n - 1
    v = np.zeros(n)
    for s in range(n - 1, -1, -1):
        s = top[s]
        if not v[s]:
            f = dfs2(s, f) - 1


dfs_main()

print(Counter(order).most_common(5))
