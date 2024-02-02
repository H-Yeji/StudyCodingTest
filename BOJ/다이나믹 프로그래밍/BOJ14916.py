import sys
n = int(sys.stdin.readline())
arr = [2, 5]

d = [100001] * (n + 1)
d[0] = 0

for i in range(2):
    for j in range(arr[i], n + 1):
        if d[j - arr[i]] != 100001:
            d[j] = min(d[j], d[j - arr[i]] + 1)


if d[n] == 100001:
    print(-1)
else:
    print(d[n])
