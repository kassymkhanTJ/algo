for _ in range(int(input())):
    n = int(input())
    s = input().strip()
    i = 0
    j = 0
    res = ""
    d = set()
    l = []
    for i in range(n):
        if s[i] in d:
            while l and l[-1] != s[i]:
                p = l.pop()
                if p in d:
                    d.remove(p)
            d.remove(s[i])
        else:
            d.add(s[i])
            l.append(s[i])
    print("".join(l))
