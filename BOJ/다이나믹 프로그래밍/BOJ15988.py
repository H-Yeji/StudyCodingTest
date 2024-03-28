import sys
input = sys.stdin.readline
n = int(input())

dp = []
dp += [0, 1, 2, 4]
for i in range(4, 1000001):
    dp.append(dp[i - 1] % 1000000009 + dp[i - 2] % 1000000009 + dp[i - 3] % 1000000009)


for _ in range(n):
    t = int(input())
    print(dp[t] % 1000000009)
