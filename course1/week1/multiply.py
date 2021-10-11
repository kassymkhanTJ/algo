def mult(a, b):
    x = []
    y = []
    while a:
        x.append(a % 10)
        a = a // 10
    while b:
        y.append(b % 10)
        b = b // 10
    res = [0 for _ in range(2 * (max(len(x), len(y))))]
    for i in range(len(x)):
        c = 0
        for j in range(len(y)):
            k = i + j
            res[k] = res[k] + x[i] * y[j] + c
            c = res[k] // 10
            res[k] %= 10
        if c:
            res[i + j + 1] = c
    n = 0
    for i in range(len(res)):
        n += res[i] * 10 ** i
    return n


a = 3141592653589793238462643383279502884197169399375105820974944592
b = 2718281828459045235360287471352662497757247093699959574966967627
# a = 234
# b = 463
print(a * b)
print(mult(a, b))
print(mult(a, b) == a * b)
