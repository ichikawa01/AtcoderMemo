def Warshall_Floid(G):


    """
    G: 隣接グラフ
    """

    inf = float('INF') 
    num_nodes = len(G)  #頂点数
    dist = [[inf]*num_nodes for _ in range(num_nodes)] #テーブルを用意

    #テーブルを初期化: 同じ頂点は重み0 かつ　隣接グラフG[From][To]=weight　を入力
    for frm in range(num_nodes):
        dist[frm][frm] = 0 #初期化1 同じ頂点は重み0
        for to, weight in G[frm]:
            dist[frm][to] = weight
    
    #フロイドワーシャル法のコア部分
    for k in range(num_nodes):
        for From in range(num_nodes):
            for To in range(num_nodes):
                if dist[From][k] + dist[k][To] < dist[From][To]:
                    dist[From][To] = dist[From][k] + dist[k][To]
    
    #負閉路の検出 dist[i][i]<0となる頂点iがあれば負閉路が存在
    NEGATIVE_CYCLE = False
    for i in range(num_nodes):
        if dist[i][i] < 0:
            NEGATIVE_CYCLE = True
            break
    
    return dist, NEGATIVE_CYCLE
