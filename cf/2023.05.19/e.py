import math

for _ in range(int(input())):
    n = int(input())
    a = list(map(lambda x: int(x) - 1, input().strip().split(' ')))
    v = [0 for _ in range(n)]
    closed = 0
    open = 0
    for i in range(n):
        if v[i] or v[a[i]]:
            continue
        while not v[i]:
            print(i, end=" ")
            v[i] = 1
            i = a[i]
        print()
        if i == a[a[i]]:
            open += 1
        else:
            print(i)
            closed += 1

    print(max(1, closed), closed + open, open, closed)
