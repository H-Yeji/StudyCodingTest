import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

sortArr = sorted(arr)
result = []

for i in range(len(arr)):
    for j in range(len(sortArr)):
        if arr[i] == sortArr[j]:
            result.append(j)
            sortArr[j] = 1001
            break


print(*result)
