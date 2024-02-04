n = int(input())
coin = list(map(int, input().split()))
coin.sort()

target = 1
# 갖고있는 화폐의 단위보다 target이 작아야만 다음 수를 만들 수 있음
# 그 전까지 화폐 단위 계속 더해가며 비교하기
for i in coin:
    # 만들 수 없는 금액을 찾으면 반복 종료
    if target < i:
        break
    target += i

print(target)
