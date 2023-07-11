c = int(input())

for _ in range(c):
    n = int(input().strip())
    l = list(map(int, input().strip().split(' ')))
    if n == 1:
        print(0)
        continue
    prev = 0
    for i in range(n // 2):
        tmp = abs(l[i] - l[n - i - 1])
        if tmp == 0:
            tmp = l[i]
        if tmp == 0:
            continue
        if prev:
            if max(tmp, prev) % min(tmp, prev) != 0:
                print(0)
                continue
            prev = min(tmp, prev)
        else:
            prev = tmp
    print(prev)
