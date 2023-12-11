n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(a, b):
    if a < 0 or a >= n or b < 0 or b >= m:
        return False

    if graph[a][b] == 0:
        # 방문 처리
        graph[a][b] = 1
        # 상하좌우 모두 재귀호출
        dfs(a - 1, b)
        dfs(a + 1, b)
        dfs(a, b - 1)
        dfs(a, b + 1)
        return True
    return False


ice_cream = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 dfs 수행
        if dfs(i, j):
            ice_cream += 1

print(ice_cream)
