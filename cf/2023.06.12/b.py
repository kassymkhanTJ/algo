for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().strip().split(' ')))
    c = 0
    res = 0
    hasZ = False
    res2 = 0
    for i in range(n):
        if l[i] <= 0:
            res2 -= l[i]
            if l[i] < 0:
                hasZ = True
            c += 1
        else:
            res2 += l[i]
            if hasZ:
                res += min(c, 1)
            hasZ = False
            c = 0
    if hasZ:
        res += min(c, 1)
    print(res2, res)


