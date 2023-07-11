c = int(input())
# while True:
for i in range(c):
    n = int(input().strip())
    l = list(map(int, input().strip().split(' ')))
    l.sort()
    res = 1
    t = 1
    prev_t = 1
    i = 1
    while i < n:
        k = l[i] - l[i - 1]
        while k == 0:
            t += 1
            i += 1
            if i == n:
                break
            k = l[i] - l[i - 1]
        if prev_t < t:
            res += t - prev_t
        if k > 1:
            res += 1
            t = 1
        prev_t = t
        t = 1
        i += 1
    print(res)

    # 1 2 2 3 3 4
