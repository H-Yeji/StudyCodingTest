num = int(input())

N = 3
s = 1

for i in range(num - 1):
    s = s * 2
    N = N + s

print(N * N)