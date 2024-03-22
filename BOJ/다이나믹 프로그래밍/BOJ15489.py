import sys
input = sys.stdin.readline

r, c, w = map(int, input().split())
n = r + w - 1

# 파스칼 삼각형 생성
dp = [[1 for _ in range(n)] for _ in range(n)]
for i in range(2, n):
    for j in range(1, i):
        dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]

cnt = 0
for i in range(r - 1, r + w - 1):
    start = c - 1
    end = c - 1 + (i - (r - 1))
    for j in range(start, end + 1):
        cnt += dp[i][j]
print(cnt)
