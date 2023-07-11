c = int(input())
for _ in range(c):
    n = int(input().strip())
    l = [list(map(int, input().strip().split(' '))) for _ in range(n)]
    a, b, c = l[0][0], l[1][0], l[2][0]
    t = b
    if a == c:
        t = a
    for i in l:
        if i[0] != t:
            print(str(t) + " " + " ".join(map(str, i)))
