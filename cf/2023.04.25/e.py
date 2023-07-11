c = int(input())

for _ in range(c):
    n = int(input().strip())
    s = input().strip()
    if n % 2 != 0:
        print(-1)
        continue
    d1 = {}
    d2 = {}
    n2 = n // 2
    k = 0
    for i in range(n2):
        j = n - i - 1
        d1[s[i]] = d1.get(s[i], 0) + 1
        d1[s[j]] = d1.get(s[j], 0) + 1
        if d1[s[i]] > n2 or d1[s[j]] > n2:
            print(-1)
            break
        if s[i] == s[j]:
            d2[s[i]] = d2.get(s[i], 0) + 1
            k += 1
    else:
        if not d2:
            print(0)
            continue
        print(max(max(d2.values()), (k + 1) // 2))
