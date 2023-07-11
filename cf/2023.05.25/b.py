import math

for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    mx = 1
    c = 1
    start = s[0]
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            c += 1
        else:
            c = 1
            mx = max(c, mx)
    mx = max(c, mx)
    print(mx + 1)
