import math

with open('input.txt', 'r') as f:
    n, k = f.readline().strip().split(' ')
    n, k = int(n), int(k)
    l = list(map(int, f.readline().strip().split(' ')))

l.sort()
a = sum(l[1:k + 1])
res = [a - k * l[0]]
j = 0
for i in range(1, n):
    if j + k < i:
        a = a + (l[i-1] * k)
        j += 1
        a = a - abs(l[j + k] - l[i])
    r = j + k
    if r == i:
        r += 1
    while r < n and l[i] - l[j] > l[r] - l[i]:
        a = a - (l[j] + l[i])
        j += 1
        a = a + (l[r] + l[i-1])
        r = j + k
        if r == i:
            r += 1
    res.append(a)
    print(res, a)

print(res)

with open('output.txt', 'w') as f:
    pass
