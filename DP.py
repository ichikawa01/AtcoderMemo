# １段または２段移動できる場合の最小コスト
def Frog1():
    N = int(input())
    h = list(map(int, input().split()))

    dp = [0] * N
    dp[1] = abs(h[1] - h[0])

    for i in range(2, N):
        dp[i] = min(dp[i-1] + abs(h[i] - h[i-1]), dp[i-2] + abs(h[i] - h[i-2]))

    print(dp[N-1])


# １からK段まで移動できる場合の最小コスト
def Frog2():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))

    dp = [10**9 + 1] * N
    dp[0] = 0
    dp[1] = abs(h[1] - h[0])

    for i in range(2, N):
        for j in range(1, K+1):
            if i - j < 0:
                break
            dp[i] = min(dp[i], dp[i-j] + abs(h[i] - h[i-j]))

    print(dp[N-1])


# グリッドの移動できる経路の本数を求める
def Grid1():

    H, W = map(int, input().split())
    A = [input() for _ in range(H)]

    dp = [[0] * W for _ in range(H)]
    dp[0][0] = 1
    MOD = 10**9+7

    for i in range(H):
        for j in range(W):
            if A[i][j] == '#':
                continue

            if i+1 < H and A[i+1][j] == '.':
                dp[i+1][j] += dp[i][j]
                dp[i+1][j] %= MOD

            if j+1 < W and A[i][j+1] == '.':
                dp[i][j+1] += dp[i][j]
                dp[i][j+1] %= MOD

    print(dp[H-1][W-1])


"""
N 個, 重さ W, 価値 V のナップサック問題
"""
# i個目まで選んだ時,重さj以下での最大価値
def knapsack1():
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
def knapsack2():
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


# コインの表の回数が裏よりも多い場合の確率
def Coin():
    N = int(input())
    P = list(map(float, input().split()))

    dp = [[0] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(N):
        for j in range(N):
            dp[i+1][j+1] += dp[i][j] * P[i]
            dp[i+1][j] += dp[i][j] * (1 - P[i])

    ans = 0
    for i in range(N//2+1, N+1):
        ans += dp[-1][i]

    print(ans)


# 寿司がN皿あり0,1,2,3個ある状態から全て食べるまでの皿選択回数（ランダム）の期待値
def Sushi():
    N = int(input())
    A = list(map(int, input().split()))
    I = A.count(1)
    J = A.count(2)
    K = A.count(3)

    # dp[N+1][N+1][N+1]
    dp = [[[0 for _ in range(310)] for _ in range(310)] for _ in range(310)]

    for k in range(N+1):
        for j in range(N+1):
            for i in range(N+1):
                total = i + j + k
                if total == 0:
                    continue

                e = N / total
                if i > 0:
                    e += dp[i-1][j][k] * i / total
                if j > 0:
                    e += dp[i+1][j-1][k] * j / total
                if k > 0:
                    e += dp[i][j+1][k-1] * k / total
                
                dp[i][j][k] = e
    print(dp[I][J][K])


# 石を取り合うゲームで先手が勝つかどうか
def stones():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    dp = [False] * (K+1)

    for i in range(1, K+1):
        for a in A:
            if i - a >= 0:
                dp[i] = dp[i] or not dp[i-a]

    print('First' if dp[K] else 'Second')


# 数列の両端の数字を取り合い、先手の最大得点
def min_max():
    N = int(input())
    A = list(map(int, input().split()))

    dp = [[0] * (N+1) for _ in range(N+1)]

    for length in range(1, N+1):
        for left in range(N - length + 1):
            right = left + length
            dp[left][right] = max(A[left] - dp[left + 1][right], A[right - 1] - dp[left][right - 1])

    print(dp[0][N])






