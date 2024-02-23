from collections import deque

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 방문 유무 확인
visited = [[False] * n for _ in range(n)]

dx = [0, 1]
dy = [1, 0]


def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        step = graph[x][y]

        # 종료 조건
        if graph[x][y] == -1:
            return True

        for i in range(2):
            nx = x + dx[i] * step
            ny = y + dy[i] * step

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))


if bfs(0, 0):
    print("HaruHaru")
else:
    print("Hing")
