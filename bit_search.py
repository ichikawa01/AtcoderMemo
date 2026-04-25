S = input()
N = len(S)
ans = 0

# Sに+を挟む方法は、Sに文字と文字の間(N-1個ある)に
# それぞれ挟むか挟まないかを決めれば決まるから2^(N-1)通りある。

# それを長さN-1のbitに対応させることで全探索することで答えを求める。
# 例: S = 12345 bit = 110 なら bit = 0110 とみなして 12+3+45 を答えに足していく。

for bit in range(1 << (N - 1)):  # 1 << (N-1) は 2^(N-1) と同じ
    s = S[0]
    for i in range(N - 1):  # どこにbitが立ってるかを確認していく
        if bit & (1 << i):  # 下からi番目にbitが立っているとき
            ans += int(s)
            s = ""
        s += S[i + 1]
    ans += int(s)
print(ans)


"""

N種類の動物園(1...N)
料金はCi
M種類の動物(1...M)を全て２回以上見る必要がある。
Kには、動物iを見ることができる動物園

ビット全探索で、どの動物園に行くかを決める。
同じ動物園に2回行く事もあるので、配列を2倍にして整理

"""

N, M = map(int, input().split())
C = list(map(int, input().split()))
K = [list(map(int, input().split())) for _ in range(M)]

# 動物園iに行ったら見ることができる動物のリスト
animals = [[] for _ in range(N * 2)]
for i in range(M):
    for j in range(K[i][0]):
        idx = K[i][j + 1] - 1
        animals[idx*2].append(i)
        animals[idx*2 + 1].append(i)

ans = float('inf')
for bit in range(1 << (N * 2)):
    view = [0] * M
    total = 0
    for i in range(N * 2):  # どこにbitが立ってるかを確認していく
        if bit & (1 << i):  # 下からi番目にbitが立っているとき
            total += C[i // 2]
            for j in animals[i]:
                view[j] += 1
    if min(view) >= 2:
        ans = min(ans, total)

print(ans)
                
