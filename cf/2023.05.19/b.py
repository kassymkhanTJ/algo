modulus = 10 ** 9 + 7
for _ in range(int(input())):
    n, k = list(map(int, input().strip().split(' ')))
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    aCopy = [(a[i], i) for i in range(n)]
    aCopy.sort()
    b.sort()
    res = [0 for _ in range(n)]
    for i in range(n):
        res[aCopy[i][1]] = b[i]
    print(*res)