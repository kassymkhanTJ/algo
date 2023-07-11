c = int(input())

for _ in range(c):
    s = input().strip()
    i = s[0]
    for j in s:
        if i != j:
            break
    else:
        print(-1)
        continue
    print(len(s) - 1)
