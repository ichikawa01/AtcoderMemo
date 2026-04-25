from atcoder.dsu import DSU

"""

    uf = DSU(N) : 初期化(Nは頂点数)
    
    uf.merge(u, v) : 「頂点uの連結成分」と「頂点vの連結成分」を結合。この連結成分の代表元を返す。

    uf.same(u, v) : u, vが同じ連結成分ならTrueを、そうでない場合はFalseを返す。

    uf.leader(u) : 頂点uの連結成分の代表元を返す。
    
    uf.size(u) : 頂点uの連結成分の頂点数を返す。

    uf.groups() : 各連結成分のリストを返す (各連結成分がそれぞれリスト、全体として2次元リスト)。

"""

# 0, u, v -> merge u and v
# 1, u, v -> u and v are same ?
N, Q = map(int, input().split())
uf = DSU(N)
for _ in range(Q):
    t, u, v = map(int, input().split())
    if t == 0:
        uf.merge(u, v)
    else:
        if uf.same(u, v):
            print(1)
        else:
            print(0)
