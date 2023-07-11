c = int(input())

for _ in range(c):
    n = int(input().strip())
    l = list(map(int, input().strip().split(' ')))
    c = 0
    m = 0
    for i in range(n):
        if l[i]:
            m = max(c, m)
            c = 0
        else:
            c += 1
    m = max(c, m)
    print(m)
