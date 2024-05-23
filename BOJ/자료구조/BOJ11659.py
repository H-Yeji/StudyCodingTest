import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

pre = [0] * (n + 1)
for i in range(n):
    # 누적합
    pre[i + 1] = pre[i] + arr[i]

for i in range(1, m + 1):
    a, b = map(int, input().split())
    print(pre[b] - pre[a - 1])

