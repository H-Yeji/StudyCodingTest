import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort(reverse=True)

'''
이진탐색으로 해결
'''
start = 0
end = max(arr)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in arr:
        if i > mid:
            total += i - mid

    if total < m:
        end = mid - 1
    else: # m과 같을 시
        result = mid
        start = mid + 1


print(result)