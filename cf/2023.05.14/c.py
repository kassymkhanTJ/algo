modulus = 10 ** 9 + 7
for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().strip().split(' '))), reverse=True)
    b = sorted(list(map(int, input().strip().split(' '))), reverse=True)
    i = 0
    res = 1
    for j in range(n):
        while i < n and a[i] > b[j]:
            i += 1
        res *= i - j
    print(res % modulus)

# [9, 8, 6, 5, 4, 2]
# [6, 5, 4, 3, 1, 1]