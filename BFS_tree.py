from collections import deque

import sys
sys.setrecursionlimit(10**7)

"""
X から Y への最短経路を計算
"""

N, X, Y = map(int, input().split()) # 複数入力
X, Y = X-1, Y-1
G = [[] for _ in range(N)]
dist = [-1] * N # 距離
prev = [-1] * N # 経路

for i in range(N-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    # 有効グラフ
    # G[u].append(v)

    # 無向グラフ
    G[u].append(v)
    G[v].append(u)

Q = deque([X])
dist[X] = 0

while Q:
    node = Q.popleft()

    for next in G[node]:
        if dist[next] == -1:
            dist[next] = dist[node] + 1
            prev[next] = node
            Q.append(next)

ans = []
now = Y

while now != -1:
    ans.append(now + 1)
    now = prev[now]

# 最短経路を出力
print(*ans[::-1])
print(dist)
print(prev)