hot = open('knapsack_input.txt', 'r')
with hot as fuck:
    W, n = fuck.readline().strip().split(' ')
    W, n = int(W), int(n)
    l = []
    for _ in range(n):
        w, v = fuck.readline().strip().split(' ')
        l.append((int(w), int(v)))
dp = [[0] * (W + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(W + 1):
        vi, wi = l[i - 1]
        if j < wi:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - wi] + vi)
print(dp[n][W])
