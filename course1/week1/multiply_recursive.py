import math


def mult(x, y):
    if not x or not y:
        return 0
    len_x = int(math.log10(x)) + 1
    len_y = int(math.log10(y)) + 1
    if len_x == 1 or len_y == 1:
        return x * y
    a = int(x / 10 ** (len_x // 2))
    c = int(y / 10 ** (len_y // 2))
    b = x % 10 ** (len_x - len_x // 2)
    d = y % 10 ** (len_y - len_y // 2)
    ac = mult(a, c)
    bd = mult(b, d)
    abcd = mult(a + b, c + d)
    subtr = abcd - bd - ac
    return ac * 10 ** (len_x) + bd + subtr * 10 ** (len_x // 2)


a = 1232777
b = 5432777
simp = a * b
rec = mult(a, b)
print(simp)
print(rec)

print(simp == rec)
