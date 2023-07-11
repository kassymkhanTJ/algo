c = int(input())
for _ in range(c):
    n, s, r = map(int, input().strip().split(' '))
    t = s - r
    m = r // (n - 1)
    l = [m for _ in range(n - 1)]
    k = r % (n - 1)
    for i in range(k):
        l[i] += 1
    l.append(t)
    print(" ".join(map(str, l)))
