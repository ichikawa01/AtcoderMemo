"""

LCS: Longest Common Subsequence（最長の部分文字列）
任意の文字を削除して、元の文字列を並べて等しくなるような文字列の長さ

dp[len(S)][len(T)] 最長の部分文字列の長さ
ans 最長の部分文字列

"""

S = input()
T = input()

dp = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]

for i in range(1, len(S)+1):
    for j in range(1, len(T)+1):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        if S[i-1] == T[j-1]:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)

# print(dp[len(S)][len(T)])


ans = ''
i, j = len(S), len(T)
while i > 0 and j > 0:
    if S[i-1] == T[j-1]:
        ans = S[i-1] + ans
        i -= 1
        j -= 1
    elif dp[i-1][j] >= dp[i][j-1]:
        i -= 1
    else:
        j -= 1

print(ans)


