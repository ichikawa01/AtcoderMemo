def topological_sort(node, input_edge):
    """トポロジカルソート

    有向グラフの順序を守るようにソートする
    閉路があるか判定も出来る
    計算量: O(E+V)

    Args:
        node (list): edge[i] = [a, b,...] iからa,b,...に辺が伸びている
        input_edge (list): input_edge[i] = iの入力辺の本数

    Returns:
        list or -1:閉路が存在しないとき
                      ソート済みのリスト
                   閉路が存在する時
                      -1   
    """
    N = len(input_edge)
    ans = [i for i in range(N) if input_edge[i] == 0]
    que = deque(ans)
    while que:
        q = que.popleft()
        for e in node[q]:
            input_edge[e] -= 1
            if input_edge[e] == 0:
                que.append(e)
                ans.append(e)
    if len(ans) == N:
        return ans
    return -1