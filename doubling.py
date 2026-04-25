def preprocess(graph, n):
    # ダブリングのための最大のビット数（2^kが時刻の上限を超えるまで）
    MAX_POW = 60  # 2^60 > 10^15 なので十分
    # ダブリングテーブル
    next_node = [[-1] * (MAX_POW + 1) for _ in range(n)]
    
    # 各ノードについて、最も重い辺の先を next_node[node][0] にセット
    for node in range(n):
        if graph[node]:
            next_node[node][0] = max(graph[node], key=lambda x: x[1])[0]

    # ダブリングテーブルの構築
    for k in range(1, MAX_POW + 1):
        for node in range(n):
            if next_node[node][k-1] != -1:
                next_node[node][k] = next_node[next_node[node][k-1]][k-1]

    return next_node

def find_location_at_time(start, time, next_node):
    # 任意の時刻における地点を求める
    pos = start
    k = 0
    while time > 0:
        if time & 1:  # time の現在のビットが1なら、その距離分だけ進む
            pos = next_node[pos][k]
        time >>= 1
        k += 1
    return pos

# 使用例
n = 5  # ノードの数
graph = [[] for _ in range(n)]
graph[0].append((1, 3))  # ノード0からノード1への重み3の辺
graph[1].append((2, 5))  # ノード1からノード2への重み5の辺
graph[2].append((3, 1))  # ノード2からノード3への重み1の辺
graph[3].append((4, 4))  # ノード3からノード4への重み4の辺
graph[4].append((0, 2))  # ノード4からノード0への重み2の辺

# 前処理
next_node = preprocess(graph, n)

# 任意の時刻 t における地点を求める
t = 10**15  # 非常に大きな時刻
start = 0   # 開始地点
result = find_location_at_time(start, t, next_node)
print(f"時刻 {t} における地点: {result}")
