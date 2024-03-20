import sys
input = sys.stdin.readline


def cal(n):
    Min = arr[0]
    for i in range(1, n):
        dp[i] = max(dp[i - 1], arr[i] - Min)
        Min = min(Min, arr[i])


n = int(input())
arr = list(map(int, input().split()))
dp = [0 for _ in range(n)]
cal(n)
print(*dp)
