from collections import deque

# N: 木Tの頂点数
# G[u] = [(w, c), ...] : 頂点uに隣接する頂点w、それを繋ぐ辺の長さc
N = int(input())
G = [[] for _ in range(N)]

# 与えられた点から最も遠い点とその距離を返すBFS
def bfs(s):
    dist = [None]*N
    que = deque([s])
    dist[s] = 0
    while que:
        v = que.popleft()
        d = dist[v]
        for w, c in G[v]:
            if dist[w] is not None:
                continue
            dist[w] = d + c
            que.append(w)
    d = max(dist)
    return dist.index(d), d

# パスu-vがこの木Tの直径(長さd)
u, _ = bfs(0)
v, d = bfs(u)
