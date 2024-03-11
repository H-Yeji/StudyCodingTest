import sys
input = sys.stdin.readline


def find_position(num):
    start = 0
    end = n - 1
    result = 0

    while start <= end:
        mid = (start + end) // 2

        if num < dot[mid]:
            end = mid - 1
        elif num > dot[mid]:
            start = mid + 1
        else:
            result = mid
            return start, end, result, 1

    return start, end, result, 0


n, m = map(int, input().split())
dot = list(map(int, input().split()))
dot.sort()
for i in range(m):
    a, b = map(int, input().split())

    # a의 위치 찾기
    start, end, result, flag = find_position(a)
    if flag == 0:
        low = start
    else:
        low = result

    # b의 위치 찾기
    start, end, result, flag = find_position(b)
    if flag == 0:
        high = end
    else:
        high = result

    # 개수 계산
    print(high - low + 1)
