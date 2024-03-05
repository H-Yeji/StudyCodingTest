import sys
input = sys.stdin.readline

n, l = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

start = arr[0]
length, cnt = 0, 0
for i in range(n):
    if arr[i] - start < l:
        length += 1
    else:
        start = arr[i]
        cnt += 1
        length = 1 # 초기화
cnt += 1 # 마지막 테이프 갯수 추가

print(cnt)
