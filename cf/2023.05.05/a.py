c = int(input())

for _ in range(c):
    n = int(input().strip())
    l = sorted(list(map(int, input().strip().split(' '))), reverse=True)
    res = 0
    i = j = 0
    while i < n:
        while j < n and l[i] == l[j]:
            j += 1
# 6 6 5 5 3 3
