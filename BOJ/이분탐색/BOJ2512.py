import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
budget = int(input())

arr.sort()

start = 0
end = max(arr)
Max = 0
while start <= end:
    mid = (start + end) // 2
    sumResult = sum(min(mid, request) for request in arr)

    if sumResult <= budget:
        Max = mid
        start = mid + 1
    elif sumResult > budget:
        end = mid - 1

print(Max)
