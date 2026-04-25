from collections import deque

def bfs_maze(maze, H, W, start, goal):
    sy, sx = start  # スタート位置
    gy, gx = goal   # ゴール位置
    
    # 移動方向（上下左右）
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 距離配列（未訪問は -1）
    dist = [[-1] * W for _ in range(H)]
    dist[sy][sx] = 0  # スタート地点の距離は 0

    # BFS 用キュー
    queue = deque([(sy, sx)])

    while queue:
        y, x = queue.popleft()  # 現在の位置

        # ゴールに到達したら距離を返す
        if (y, x) == (gy, gx):
            return dist[y][x]

        # 4方向に移動
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < H and 0 <= nx < W and maze[ny][nx] != '#' and dist[ny][nx] == -1:
                dist[ny][nx] = dist[y][x] + 1  # 距離更新
                queue.append((ny, nx))

    return -1  # ゴールに到達できない場合

# 迷路の入力例
H, W = 5, 5
maze = [input() for _ in range(H)]

# スタートとゴールの座標を探す
start, goal = None, None
for i in range(H):
    for j in range(W):
        if maze[i][j] == 'S':
            start = (i, j)
        elif maze[i][j] == 'G':
            goal = (i, j)

# BFS 実行
result = bfs_maze(maze, H, W, start, goal)
print("最短距離:", result)
