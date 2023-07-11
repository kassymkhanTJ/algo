c = int(input())
for _ in range(c):
    n = int(input())
    if n == 1:
        print(1)
        continue
    l = [i for i in range(1, n + 1)]
    if n % 2 == 0:
        for i in range(0, n, 2):
            print(n - i - 1, end=" ")
            print(n - i, end=" ")
    else:
        print(-1)
        continue
    print()
