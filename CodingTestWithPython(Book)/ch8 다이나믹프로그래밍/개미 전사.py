n = int(input())
arr = list(map(int, input().split()))

d = []
d.append(arr[0])
d.append(max(d[0], arr[1]))
# 다이나믹 프로그래밍 진행 (보텀업) 
for i in range(2, n):
    d.append(max(d[i - 1], (arr[i - 2] + arr[i])))


print(d[n - 1])
