"""

    op = 演算 (関数オブジェクト)
    e = 単位元 (関数オブジェクト)
    n = 要素数
    v = 対象の列 (vを与えない場合、全ノードが単位元のセグ木が構築)

    set(p, x) : Ap -> x に更新
    prod(l, r) : [l, r)の総積を取得
    all_prod() : 全ノードの総積を取得
    get(p) : pが与えられた時、Apを取得

    max_right(l, f) : f(prod(l, r)) = True となる最大のr
    f(prod(l, r)) = True かつ f(prod(l, r+1)) = False を満たすrのうちのいずれか1つ(or r = N)
    例えば、配列のl以降で値が10以上になる最小のインデックスの取得（満たさない最大と置き換える）

    min_left(r, f) : f(prod(l, r)) = True となる最小のl
    max_rightの左右逆バージョンのイメージ


"""

#####segTree#####
class SegTree:

    def __init__(self, op, e, n, v=None):
        self._n = n
        self._op = op
        self._e = e
        self._log = (n - 1).bit_length()
        self._size = 1 << self._log
        self._d = [self._e()] * (2 * self._size)
        if v is not None:
            for i in range(self._n):
                self._d[self._size + i] = v[i]
            for i in range(self._size - 1, 0, -1):
                self._update(i)
    
    def set(self, p, x):
        assert 0 <= p < self._n
        p += self._size
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)
    
    def get(self, p):
        assert 0 <= p < self._n
        return self._d[p + self._size]

    def prod(self, l, r):
        assert 0 <= l <= r <= self._n
        sml, smr = self._e(), self._e()
        l += self._size
        r += self._size
        while l < r:
            if l & 1:
                sml = self._op(sml, self._d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self._op(self._d[r], smr)
            l >>= 1
            r >>= 1
        return self._op(sml, smr)
    
    def all_prod(self):
        return self._d[1]

    def _update(self, k):
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])

    def max_right(self, l, f):
        assert 0 <= l <= self._n
        assert f(self._e())
        if l == self._n: return self._n
        l += self._size # 葉に移動
        sm = self._e() # 確定した区間の積を保持する変数
        while True:
            while l % 2 == 0: l >>= 1 #　右ノードになるまで
            if not f(self._op(sm, self._d[l])):
                # STEP2
                while l < self._size:
                    l <<= 1
                    if f(self._op(sm, self._d[l])):
                        sm = self._op(sm, self._d[l])
                        l += 1
                return l - self._size
            sm = self._op(sm, self._d[l])
            l += 1
            if l & -l == l: break # f(prod(l, N))=Trueが確定
        return self._n

    def min_left(self, r, f):
        assert 0 <= r <= self._n
        assert f(self._e())
        if r == 0: return 0
        r += self._size
        sm = self._e()
        while True:
            r -= 1
            while r > 1 and r % 2: r >>= 1 # 左子ノードになるまで
            if not f(self._op(self._d[r], sm)):
                # STEP2
                while r < self._size:
                    r = 2 * r + 1 # 右子ノードに移動
                    if f(self._op(self._d[r], sm)):
                        sm = self._op(self._d[r], sm)
                        r -= 1
                return r + 1 - self._size
            sm = self._op(self._d[r], sm)
            if r & -r == r: break
        return 0

#################


# 使い方の例

n = 5
A = [3, 2, 1, 4, 5]

def op(x, y):
    
    # return max(x, y)
    # return min(x, y)
    return x + y



def e():
    # return float('-inf')
    # return float('inf')
    return 0