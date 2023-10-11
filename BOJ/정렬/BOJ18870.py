import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arrSet = sorted(list(set(arr))) #중복제거 + 정렬

#딕셔너리로 {arr숫자 : 해당 숫자보다 작은 수의 개수(i)}
dic = {arrSet[i]:i for i in range(len(arrSet))}
for i in arr:
    print(dic[i], end=" ")





