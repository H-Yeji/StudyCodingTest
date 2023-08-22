n = int(input())
arr = list(map(int, input().split()))
'''
#단순 풀이 버전 
result = 0

for i in range(len(arr)):
    cnt = 0
    for j in range(1, arr[i]+1):
        if arr[i] % j == 0:
            cnt += 1

    if cnt == 2:
        result += 1

print(result)
'''
#더 효율적인 버전 (시간 복잡도)
result = 0

for i in range(len(arr)):
    arr2 = []
    for j in range(1, int(arr[i]**(1/2))+1):
        if arr[i] % j == 0:
            arr2.append(arr[i])
            if j**2 != arr[i]:
                arr2.append(arr[i] // j)

    if len(arr2) == 2:
        result += 1

print(result)
