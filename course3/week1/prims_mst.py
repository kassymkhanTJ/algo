import math

hot = open('input_2.txt', 'r')
with hot as fuck:
    n, m = fuck.readline().strip().split()
    n, m = int(n), int(m)
    G = set()
    for _ in range(m):
        v, w, l = fuck.readline().strip().split()
        v, w, l = int(v), int(w), int(l)
        G.add((v, w, l))
X = {1}

res = 0
while True:
    l_ = math.inf
    for v, w, l in G:
        if (v in X and w not in X) or (w in X and v not in X):
            if l < l_:
                v_, w_, l_ = v, w, l
    if math.isinf(l_):
        break
    X.add(v_)
    X.add(w_)
    G.remove((v_, w_, l_))
    res += l_
print(res)
