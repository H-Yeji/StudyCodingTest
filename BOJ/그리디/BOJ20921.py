import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(range(1, n + 1))

cnt = 0
total = 0
while total < k:
    if k - total < n - cnt:
        result = (cnt + (k - total)) % n
        tmp = arr[result]
        for i in range(result, cnt, -1):
            arr[i] = arr[i - 1]
        arr[cnt] = tmp
        total += (k - total)

    else:
        tmp = arr[n - 1]
        for i in range(n - 1, cnt, -1):
            arr[i] = arr[i - 1]
        arr[cnt] = tmp
        cnt += 1
        total += (n - cnt)

print(*arr)
