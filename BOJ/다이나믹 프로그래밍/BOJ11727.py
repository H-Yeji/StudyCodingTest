import sys

n = int(sys.stdin.readline())

d = [0]
d.append(1)
d.append(3)
for i in range(3, n + 1):
    d.append((d[i - 1] + d[i - 2] * 2) % 10007)


print(d[n])
