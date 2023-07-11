from math import acos

pi = "314159265358979323846264338327"
c = int(input())
for _ in range(c):
    s = input().strip()
    for i in range(len(s)):
        if s[i] != pi[i]:
            print(i)
            break
    else:
        print(len(s))
