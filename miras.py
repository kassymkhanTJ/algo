l = [1, 2]
k = 3


def rec(s, k):
    if k == 0:
        print(s)
        return
    for i in l:
        s.append(i)
        rec(s, k - 1)
        s.pop()


rec([], k)
