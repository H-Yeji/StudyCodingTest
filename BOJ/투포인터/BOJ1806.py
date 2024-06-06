import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, 0
result = 0
minLen = 99999999999

while end <= n:
    if result >= m:
        minLen = min(minLen, end - start)
        result -= arr[start]
        start += 1
    else:
        if end < n:
            result += arr[end]
            end += 1
        else:
            break

if minLen == 99999999999:
    print(0)
else:
    print(minLen)
