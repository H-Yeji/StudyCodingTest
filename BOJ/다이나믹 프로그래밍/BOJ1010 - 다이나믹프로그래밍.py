import sys
input = sys.stdin.readline


def cal(n, m):
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for j in range(m + 1):
        dp[0][j] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]

    return dp[n][m]


N = int(input())
for i in range(N):
    n, m = map(int, input().split())
    print(cal(n, m))
