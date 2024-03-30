import sys
input = sys.stdin.readline

n = int(input())
result = list(map(int, input().split()))
arr = [0] * (n + 3)
cnt = 0
for i in range(len(result)):
    if result[i] != arr[i]:
        for j in range(3):
            if arr[i + j] == 0:
                arr[i + j] = 1
            else:
                arr[i + j] = 0
        cnt += 1

print(cnt)
