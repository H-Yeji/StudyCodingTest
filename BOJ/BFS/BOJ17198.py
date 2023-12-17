from collections import deque

graph = [list(map(str, input())) for _ in range(10)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= 10 or ny >= 10:
                continue
            if graph[nx][ny] == 'R':
                continue
            if graph[nx][ny] == '.':
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
            if graph[nx][ny] == 'L':
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
                a = nx
                b = ny
                break
    return graph[a][b]


res = 0
for i in range(10):
    for j in range(10):
        if graph[i][j] == 'B':
            res = bfs(i, j)


print(res - 2)

