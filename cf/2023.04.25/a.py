c = int(input())
for _ in range(c):
    n, t = map(int, input().strip().split(' '))
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    m = 0
    ans = -1
    for i in range(n):
        if a[i] + i <= t and b[i] > m:
            m = b[i]
            ans = i + 1
    print(ans)
