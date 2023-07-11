import math

for _ in range(int(input())):
    n, k = list(map(int, input().strip().split(' ')))
    if n < k or n % k != 0:
        print(1)
        print(n)
        continue
    print(2)
    print(n - 1, 1)
