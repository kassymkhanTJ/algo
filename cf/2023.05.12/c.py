c = int(input())

for _ in range(c):
    n = int(input())
    l = list(map(int, input().strip().split(' ')))
    l2 = [l[0]]
    for i in range(1, n):
        if l[i] == l2[-1]:
            continue
        l2.append(l[i])
    print(l2)
    if len(l2) == 1:
        print(1)
        continue
    ans = 2
    for i in range(1, len(l2) - 1):
        if l2[i - 1] < l2[i] > l2[i + 1] or l2[i - 1] > l2[i] < l2[i + 1]:
            print(l2[i])
            ans += 1
    print(ans)
"""
1
7
5 4 2 100 2 1 4
"""