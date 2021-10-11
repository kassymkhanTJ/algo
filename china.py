c = int(input())
for _ in range(c):
    n, a, b = input().strip().split()
    n, a, b = int(n), int(a), int(b)
    s = input().strip()
    if a + b >= 0:
        print((a + b) * n)
    else:
        zeros = 0
        for i in s:
            if i == '0':
                zeros += 1
        i = '0'
        if zeros > n / 2:
            i = '1'
        for j in s:
            0110011100
