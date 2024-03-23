import sys
input = sys.stdin.readline

n = int(input())
t = [0 for _ in range(n + 1)]
p = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    t[i], p[i] = map(int, input().split())


dp = [0] * (n + 2)
for i in range(n, 0, -1): # 뒤에부터 역순으로 처리
    if i + t[i] <= n + 1: # 해당 상담을 처리할 수 있는 경우
        dp[i] = max(p[i] + dp[i + t[i]], dp[i + 1])
    else: # 날짜가 부족해서 해당 상담을 처리할 수 없는 걍우
        dp[i] = dp[i + 1]
print(dp[1])
