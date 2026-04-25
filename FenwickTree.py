from atcoder.fenwicktree import FenwickTree

"""

    ft = FenwickTree(N) : 初期化 (値がすべて 0 で長さ N のリスト)

    ft.add(i, v) : Ai の値に v を加算

    ft.sum(l, r) : 半開区間 [l, r) の値の総和を返す

"""

# 0, p, x -> Ap += x
# 1, l, r -> sum(l, l+1, ..., r-1)
# O(logN)

N, Q = map(int, input().split())
a = list(map(int, input().split()))

ft = FenwickTree(N)
for i, el in enumerate(a):
    ft.add(i, el)

for _ in range(Q):
    t, a, b = map(int, input().split())
    if t == 0:
        ft.add(a, b)
    elif t == 1:
        print(ft.sum(a, b))
