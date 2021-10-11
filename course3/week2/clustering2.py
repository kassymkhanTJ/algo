def union(a, c):
    b[find(a)] = find(c)


def find(a):
    if b[a] == -1:
        b[a] = a
    while a != b[a]:
        b[a] = b[b[a]]
        a = b[a]
    return a


def gen(t, d, lvl=1, cluster=None):
    if cluster is None:
        cluster = t
    for i in range(blen):
        nt = t ^ (1 << i)
        if nt not in d:
            d[nt] = []
        d[nt].append(cluster)
        if lvl < 2:
            gen(nt, d, lvl=lvl + 1, cluster=t)


p = '/Users/kasimtj/coursera/course3/week2/input_2.txt'
hot = open(p, 'r')

with hot as fuck:
    n, blen = fuck.readline().strip().split(' ')
    n, blen = int(n), int(blen)
    d = {}
    l = set()
    for i in range(n):
        t = int(''.join(fuck.readline().strip().split(' ')), 2)
        gen(t, d)
        l.add(t)

b = [-1 for _ in range(2 ** blen)]

for t in l:
    for i in d[t]:
        if i in l:
            union(i, t)
        for j in d[i]:
            if j in l:
                union(j, t)

s = set([find(i) for i in l])
print(len(s))


def pprint(*args):
    args = [bin(i) for i in args]
    nargs = [' '.join(list(args[0][2:]))]
    if len(args) < 2:
        return print(*nargs)
    for arg in args[1:]:
        nargs.append('-')
        nargs.append(' '.join(list(arg[2:])))
    return print(*nargs)

# for i in l:
#     if find(i) != i:
#         pprint(i, find(i))
#         pprint(*[j for j in d[i] if j in l])
#         print()
