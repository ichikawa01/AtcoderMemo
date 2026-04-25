from atcoder.math import floor_sum

# O(logM)

# sigma i=[0,n-1] 床関数(a*i+b / m)

T = int(input())
for _ in range(T):
    N, M, A, B = map(int, input().split())
    print(floor_sum(N, M, A, B))
