c = int(input())
for _ in range(c):
    n = int(input().strip())
    l = list(map(float, input().strip().split(' ')))
    m1 = []
    m2 = []
    s1 = 0.0
    s2 = 0.0
    for i in range(n - 1):
        s1 += l[i]
        s2 += l[n - i - 1]
        m1.append(s1 / (i + 1))
        m2.append(s2 / (i + 1))
    print(max(list(map(sum, zip(m1, reversed(m2))))))