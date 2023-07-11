import heapq
for _ in range(int(input())):
    n = int(input())
    l = sorted(list(map(int, input().strip().split(' '))))
    res = 0
    for i in range(n // 2):
        res += l[-i - 1] - l[i]
    print(res)


