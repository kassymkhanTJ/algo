c = int(input())

for _ in range(c):
    s = input().strip()
    d = {}
    for i in s:
        d[i] = d.get(i, 0) + 1
    if len(d) == 1 or len(d) == 2 and min(list(d.values())) == 1:
        print("NO")
    else:
        print("YES")
