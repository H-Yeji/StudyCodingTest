import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(n - 1):
    s = i + 1
    e = n - 1
    # 시작부터 b[start]보다 작은 경우
    if a[i] < b[s]:
        print(0, end=" ")
        continue
    # 시작부터 b[end]보다 큰 경우
    if a[i] >= b[e]:
        print(n - (i + 1), end=" ")
        continue

    # 두 경우 모두 아니면 이분탐색
    result = -1
    while s <= e:
        mid = (s + e) // 2
        if a[i] >= b[mid]:
            result = mid + 1
            s = mid + 1
        else:
            e = mid - 1
    print(result - i - 1, end=" ")
print(0)
