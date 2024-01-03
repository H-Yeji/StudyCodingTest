import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
arrN = list(map(int, sys.stdin.readline().split()))
arrN.sort()

cnt = 0
i, j = 0, n - 1
while i < j:
    if arrN[i] + arrN[j] == m:
        cnt += 1
        i += 1
        j -= 1
    elif arrN[i] + arrN[j] < m:
        i += 1
    else:
        j -= 1


print(cnt)
