def solve(l, j, ind):
    if not ind:
        return 0
    if j == len(l[0]):
        return len(ind)
    return solve(l, j + 1, [i for i in ind if l[i][j] == l[0][j]])


c = int(input())
for _ in range(c):
    n, k = list(map(int, input().strip().split(' ')))
    l = [input().strip() for _ in range(n)]
    l2 = [i for i in range(n)]
    print(solve(l, 0, l2))
