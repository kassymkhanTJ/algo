for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().strip().split(' ')))
    mx = max(l)
    mn = min(l)
    if mn < 0:
        print(mn)
    else:
        print(mx)
