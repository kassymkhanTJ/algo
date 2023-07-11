n, q = list(map(int, input().strip().split(' ')))
l = sorted(list(map(int, input().strip().split(' '))))
l2 = list(map(int, input().strip().split(' ')))
m = l[0]
n2 = 2 * n
res = []
for j in range(1, len(l2) + 1):
    q = l2[j - 1]
    if q <= n:
        if l[0] < l[q - 1]:
            res.append(l[0] + j)
        elif q < n and l[q] == l[q - 1]:
            res.append(l[q] + j)
        else:
            res.append(l[q - 1] + j)
    else:
        if (q - n) % 2 == 0:
            res.append(l[0] + j)
        elif j + l[0] < l[-1]:
            res.append(l[0] + j)
        else:
            res.append(l[-1])
print(*res)
