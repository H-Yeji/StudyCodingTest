N = int(input())
arr = []
for i in range(N):
    x, y = map(int, input().split())
    arr.append([x, y])

for x, y in sorted(arr):
    print(x, y)
