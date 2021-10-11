hot = open('input2.txt', 'r')
with hot as fuck:
    n = int(fuck.readline().strip())
    l = []
    for _ in range(n):
        l.append(int(fuck.readline().strip()))

res = [0, l[0]]

for i in range(1, n):
    res.append(max(res[i], res[i - 1] + l[i]))
i = n - 1
res2 = [0 for _ in range(n)]
while i > 0:
    if res[i] >= res[i - 1] + l[i]:
        i -= 1
    else:
        res2[i] = 1
        i -= 2
print(i)
if i == 0:
    res2[i] = 1

print(res)
print(res[-1] == sum([l[i] for i in range(n) if res2[i]]))
res3 = [res2[i-1] for i in (1, 2, 3, 4, 17, 117, 517, 997)]
print(''.join(map(str, res3)))
