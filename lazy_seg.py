from atcoder.lazysegtree import LazySegTree

# 1. 区間加算(最小値、最大値、区間和)
def op(x, y):
    # min, max, x+y
    return min(x, y)
def mapping(up, lo):
    return up + lo
def composition(func_upper, func_lower):
    return func_upper + func_lower

# inf, -inf, 0
e = float('inf')
id_ = 0
lst = [1, 2, 3, 4, 5]
# (初期リストlst)
seg = LazySegTree(op, e, mapping, composition, id_, lst)



# 2. 区間変更(最小値、最大値、区間和)
ID = float('inf')
def op(x, y):
# min, max, x+y
    return min(x, y)

def mapping(func, ele):
    if func == ID:
        return ele
    else:
        return func

def composition(func_upper, func_lower):
    if func_upper == ID:
        return func_lower
    else:
        return func_upper

# inf, -inf, 0
e = float('inf')
id_ = ID
# (初期リストlst)
seg = LazySegTree(op, e, mapping, composition, id_, lst)



# 簡易メソッド
"""

    seg.set(p, x) : Ap <- x
    
    seg.apply(l, r, x) : [l, r)の要素に対して次の操作
    ・区間加算 : Ai <- Ai + x (i = l, l+1, ..., r-1)
    ・区間変更 : Ai <- x (i = l, l+1, ..., r-1)

    seg.prod(l, r) : [l, r)の総積(最小値、最大値、区間和)を取得

    seg.get(p) : p番目の要素(0-index)の値を得る

"""