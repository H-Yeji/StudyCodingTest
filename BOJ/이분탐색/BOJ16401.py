import sys
input = sys.stdin.readline

m, n = map(int, input().split())
length = list(map(int, input().split()))

start, end = 1, max(length)
Max = 0
while start <= end:
    mid = (start + end) // 2
    result = 0

    # 몫 구하기
    for i in range(n):
        result += length[i] // mid

    if result >= m:
        Max = max(Max, mid)
        start = mid + 1
    else:
        end = mid - 1

print(Max)
