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

'''
순차 정렬로 풀어서 시간 초과된 코드 

maxH = arr[0] # 제일 큰 숫자부터 시작
while maxH > 0:
    sumM = 0
    for i in arr:
        if (i - maxH) > 0: # 자르고 남는 떡이 있을 때만 반복
            sumM += (i - maxH)
        else: # 남는 떡이 없으면 중단
            break
    if sumM == m:
        break
    maxH -= 1


print(maxH)
'''