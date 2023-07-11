import math


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    return True


for _ in range(int(input())):
    n, m = list(map(int, input().strip().split(' ')))
    nIsPrime = is_prime(n)
    mIsPrime = is_prime(m)
    end = n * m
    if nIsPrime and mIsPrime:
        for i in range(1, n // 2 + 1):
            start = m * (i - 1) + 1
            l = [start for start in range(start, start + m)]
            print(*l)
            end = m * (n - i) + 1
            l = [end for end in range(end, end + m)]
            print(*l)
        start = m * (n // 2 + 1)
        print(start, end=' ')
        print(*[i for i in range(start - m + 1, start)])
    elif nIsPrime:
        for i in range(1, n + 1):
            start = m * (i - 1) + 1
            l = [start for start in range(start, start + m)]
            print(*l)
    elif mIsPrime:
        for i in range(1, n + 1):
            start = m * (i - 1) + 1
            l = [start for start in range(start, start + m)]
            print(*l)
