import math

while True:
    m, d, l, n = input().strip().split(' ')
    m, d, l, n = int(m), float(d), float(l), int(n)
    if m < 0:
        break
    depr = []
    for _ in range(n):
        month, perc = input().strip().split(' ')
        depr.append((int(month), float(perc)))
    j = 0
    l += d
    o = l
    drop = 1
    for i in range(m):
        if j < n and i == depr[j][0]:
            drop = 1 - depr[j][1]
            j += 1
        l *= drop
        o -= d
        print(o, l, drop)
        if o < l:
            print(i)
            break
    print(i)

"""
30 500.0 15000.0 3
0 .10
1 .03
3 .002
12 500.0 9999.99 2
0 .05
2 .1
60 2400.0 30000.0 3
0 .2
1 .05
12 .025
-99 0 17000 1

"""
