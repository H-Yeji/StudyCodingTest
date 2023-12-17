from collections import deque

n, m = map(int, input().split())
graph = [list(map(str, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = '.'

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == '.':
                continue
            if graph[nx][ny] == '#':
                q.append((nx, ny))
                graph[nx][ny] = '.'

    return 1


res = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == '#':
            res += bfs(i, j)

print(res)
