import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))
result = []

# card 정렬
card.sort()
set(card)
for num in nums:
    start = 0
    end = len(card) - 1
    flag = 0

    # 이분 탐색
    while start <= end:
        mid = (start + end) // 2

        if card[mid] == num:
            result.append(1)
            flag = 1
            break
        elif card[mid] < num:
            start = mid + 1
        else:
            end = mid - 1

    if flag == 0:
        result.append(0)


print(*result)
