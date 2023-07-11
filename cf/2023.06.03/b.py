import math
for _ in range(int(input())):
    n, k = list(map(int, input().strip().split(' ')))
    if n >= (2 ** (k)):
        tmpRes = (2 ** (k))
        print(tmpRes)
        continue
    res = 0
    while n > 1:
        num = int(math.log2(n))
        tmpRes = 2 ** num - 1
        n -= tmpRes
        res += tmpRes
        print(tmpRes, n)
    print(res + 2)

# 1 2 4 8 16 32 64 128
# 0 1
"""
1
179 100
"""