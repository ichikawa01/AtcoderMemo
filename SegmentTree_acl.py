from atcoder.segtree import SegTree

# O(logN)
"""

    st = SegTree(op, e, v) : セグメントツリーを構築する。
    op : 区間の演算につかう関数
    e : 単位元
    v には list 型か int 型を入れる。list 型の場合はそのリストをそのまま入り、
    int 型の場合はすべての要素が単位元 e で長さ v のリストになる。


    st.set(p, x) : Ap = x

    st.get(p) : A の p 番目の要素を返す。


    st.prod(l, r) : 半開区間 [l:r) における演算の結果を返す。

    st.all_prod() : リスト全体における演算の結果を返す。

    st.max_right(p, func) : セグメントツリー上で二分探索をする。 
    p <= i を満たす i の中で、関数 func を満たす最大の i を返す。

    st.min_left(p, func) : セグメントツリー上で二分探索をする。 
    i < pを満たす i の中で、関数 func を満たす最小の i を返す。

"""

N, Q = map(int, input().split())
A = list(map(int, input().split()))

st = SegTree(max, -1, A)

for _ in range(Q):
    t, x, y = map(int, input().split())
    if t == 1:
        st.set(x - 1, y)
    elif t == 2:
        print(st.prod(x - 1, y))
    else:
        print(st.max_right(x - 1, lambda p: p < y) + 1)
