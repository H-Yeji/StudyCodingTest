n = int(input())
arr = list(map(int, input().split()))
arr.sort() # 정렬

group = 0
cnt = 0
for i in arr: # 순서대로 모험도 가지고 계산
    cnt += 1 # 현재 그룹에 해당 모험가 포함시키기
    if cnt >= i: # 현재 그룹에 포함된 모험가 수가 현재 공포도 이상이면 그룹 결성
        group += 1
        cnt = 0 # 초기화 

print(group)
