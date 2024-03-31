import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a, b = [], []
for i in range(n):
    a.append(list(map(int, input().strip())))
for i in range(n):
    b.append(list(map(int, input().strip())))

# 행렬 a 변환
cnt = 0
for i in range(n):
    for j in range(m):
        if (i + 2) < n and (j + 2) < m:
            if a[i][j] != b[i][j]:
                for s in range(3):
                    for t in range(3):
                        if (i + s) >= n or (j + t) >= m:
                            continue
                        if a[i + s][j + t] == 1:
                            a[i + s][j + t] = 0
                        else:
                            a[i + s][j + t] = 1
                cnt += 1

if a == b:
    print(cnt)
else:
    print(-1)
