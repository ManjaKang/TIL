# LCS알고리즘을 이용한 풀이
# PyPy 540ms

A = input()
B = input()
dp = [[0] * len(A) for _ in range(len(B))]

# 알고리즘을 진행하기 위해 각 행와 열의 첫째 칸을 채움
for i in range(len(B)):
    if B[i] == A[0]:
        dp[i][0] = 1

for j in range(len(A)):
    if A[j] == B[0]:
        dp[0][j] = 1

# LCS알고리즘 진행
for i in range(1, len(B)):
    for j in range(1, len(A)):
        if B[i] == A[j]:
            dp[i][j] = dp[i-1][j-1] + 1

ans = 0
for i in range(len(B)):
    ans = max(ans, max(dp[i]))
print(ans)
