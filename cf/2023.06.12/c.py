for _ in range(int(input())):
    n = int(input())
    tree = [[] for i in range(n)]
    for _ in range(n - 1):
        a, b = list(map(int, input().strip().split(' ')))
        a -= 1
        b -= 1
        if a < b:
            tree[a].append(b)
        else:
            tree[b].append(a)
    q = int(input())
    d = {}
    print(tree)
    for _ in range(q):
        a, b = list(map(int, input().strip().split(' ')))
        A = 0
        B = 0
        a -= 1
        b -= 1

        l = [a]
        while l:
            a = l.pop()
            if tree[a]:
                l.extend(tree[a])
            else:
                A += 1

        l = [b]
        while l:
            b = l.pop()
            if tree[b]:
                l.extend(tree[b])
            else:
                B += 1
        print(A * B)
