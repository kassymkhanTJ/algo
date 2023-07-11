c = int(input())


def calc(n, m):
    if n < m:
        return 0
    elif n == m:
        return 1
    if n % 3 == 0:
        x = n // 3
        return calc(x, m) or calc(x + x, m)
    return 0


for _ in range(c):
    n, m = list(map(int, input().strip().split(' ')))
    if n < m:
        print("NO")
        continue
    if calc(n, m):
        print("YES")
    else:
        print("NO")
