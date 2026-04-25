"""

N 個, 重さ W, 価値 V のナップサック問題

"""



# i個目まで選んだ時,重さj以下での最大価値

N, W = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(1, N+1):
    for j in range(W + 1):
        w, v = items[i-1]
        if j - w >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][W])



# Wが大きい場合
# i個目まで選んだ時,価値がjになる最小の重さの総和
N, W = map(int, input().split())
weight, value = [], []
for i in range(N):
    w, v = map(int, input().split())
    weight.append(w)
    value.append(v)

dp = [[float('INF') for _ in range(10**5 + 1)] for _ in range(N + 1)]
dp[0][0] = 0

for i in range(1, N+1):
    for j in range(10**5 + 1):
        dp[i][j] = dp[i-1][j]
        if j - value[i-1] >= 0:
            dp[i][j] = min(dp[i][j], dp[i-1][j-value[i-1]] + weight[i-1])

for i in range(10**5, -1, -1):
    if dp[N][i] <= W:
        print(i)
        break

