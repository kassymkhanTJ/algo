c = int(input())

for _ in range(c):
    s = input().strip()
    count = 0
    for i, j in zip(s, "codeforces"):
        if i != j:
            count += 1
    print(count)
