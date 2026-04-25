
"""

再帰で最長経路を求める
メモ化再帰で効率化、経路の長さと道順を求められる
最短経路だったら比較の仕方を変えるか、BFSで求める

"""
from collections import deque
import sys
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
G = [[] for _ in range(N)]
prev = [-1] * N

for _ in range(M):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)

visited = [0] * N  # 0: 未訪問, 1: 訪問中, 2: 完了
dp = [-1] * N  # メモ化
has_cycle = False  # 閉路フラグ

def dfs(v):
    global has_cycle
    if visited[v] == 1:
        has_cycle = True
        return 0
    if visited[v] == 2:
        return dp[v]

    visited[v] = 1  # 訪問中

    max_length = 0
    best_next = -1

    for next in G[v]:
        length = dfs(next) + 1
        if length > max_length:
            max_length = length
            best_next = next

    visited[v] = 2  # 完了
    dp[v] = max_length
    prev[v] = best_next
    return max_length

# 最長経路を探す
start = -1
max_length = 0

for i in range(N):
    if visited[i] == 0:
        length = dfs(i)
        if length > max_length:
            max_length = length
            start = i

# 閉路ありなら出力して終了
if has_cycle:
    print("閉路あり")
else:
    path = []
    now = start
    while now != -1:
        path.append(now + 1)
        now = prev[now]

    print(max_length)
    # print(path)

    now = prev[now]

print(max_length)
# print(path)

