c = int(input())

# 10 - 6 = 4
# 15 - 10 = 5
# 21 - 15 = 6

for _ in range(c):
    n = int(input().strip())
    sqr = n * n
    x = (n * (n + 1)) // 2
    print(2 * x + 2 + n)
