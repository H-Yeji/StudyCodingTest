import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [[1 for _ in range(n + 1)] for _ in range(n + 1)]
for i in range(2, n + 1):
    for j in range(1, i):
        dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
print(dp[n - 1][m - 1])
