c = int(input())

for _ in range(c):
    n = int(input().strip())
    if n % 2 != 0 and n != 1:
        print(-1)
        continue
    res = []
    i = 0
    j = n - 1
    for k in range(1, n // 2 + 1):
        res.append(i + n * k)
        res.append(j + n * k)
        i += 1
        j -= 1
    print(n, end=' ')
    for i in range(1, len(res)):
        print(res[i] - res[i - 1], end=' ')
    print()
# 6 5  2  3  4  1
# 6 11 13 16 20 21
# 0 5  1  4  2  3
