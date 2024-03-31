import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a, b = [], []
for i in range(n):
    a.append(list(input().strip()))
for i in range(n):
    b.append(list(input().strip()))

# str to int
for i in range(n):
    for j in range(m):
        a[i][j] = int(a[i][j])
        b[i][j] = int(b[i][j])

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

# a와 b가 일치한지 확인
flag = 0
for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            flag = 1
            break
    if flag == 1:
        break

if flag == 1:
    print(-1)
else:
    print(cnt)
