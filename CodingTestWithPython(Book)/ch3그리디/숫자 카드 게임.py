N, M = map(int, input().split())
result = 0

for _ in range(N):
    arr = list(map(int, input().split()))
    minNum = min(arr)
    result = max(minNum, result)

print(result)
