# int 入力
N = int(input())
N, M = map(int, input().split()) # 複数入力
A = list(map(int, input().split())) # 横入力
A = [int(input()) for _ in range(N)] # 縦入力
A = [list(map(int, input().split())) for _ in range(N)] # 行列（複数リスト）で入力


# str 入力
N = input()
N, M = input().split() # 複数入力
A = list(map(str, input().split)) # 横入力
A = [input() for _ in range(N)] # 縦入力
A = [list(map(str, input().split())) for _ in range(N)] # 行列（複数リスト）で入力
