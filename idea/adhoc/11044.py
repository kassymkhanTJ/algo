import math

for _ in range(int(input())):
    n, m = list(map(int, input().strip().split(' ')))
    print(math.ceil((n - 2) / 3) * math.ceil((m - 2) / 3))
