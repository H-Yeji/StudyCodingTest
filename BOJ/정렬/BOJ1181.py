import sys
n = int(sys.stdin.readline())
arr = []
arr_len = []
for _ in range(n):
    arr.append(sys.stdin.readline())

#중복제거
arr = list(set(arr))
#사전순 정렬
arr.sort()
#길이 정렬
arr.sort(key=len)

for i in arr:
    print(i, end="")


