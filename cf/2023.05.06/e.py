c = int(input())


def find(i, l):
    if l[i] == i:
        return i
    l[i] = find(l[i], l)
    return l[i]


def union(i, j, l):
    i = find(i, l)
    j = find(j, l)
    l[j] = i
    return i, j


for _ in range(c):
    n, m = list(map(int, input().strip().split(' ')))
    matr = []
    for _ in range(n):
        matr.extend(list(map(int, input().strip().split(' '))))
    l = [i for i in range(n * m)]
    for i in range(n):
        for j in range(m):
            ind = i * m + j
            if matr[ind]:
                if j + 1 < m and matr[ind + 1]:
                    rootI, rootJ = union(ind, ind + 1, l)
                    if rootI != rootJ:
                        matr[rootI] += matr[rootJ]
                newInd = ind + m
                if i + 1 < n and matr[newInd]:
                    rootI, rootJ = union(ind, newInd, l)
                    if rootI != rootJ:
                        matr[rootI] += matr[rootJ]
    print(max(matr), matr, l)
