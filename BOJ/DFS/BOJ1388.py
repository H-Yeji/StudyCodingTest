n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(str, input())))


def dfs1(a, b):
    # 방을 벗어나는 조건
    if a < 0 or a >= n or b < 0 or b >= m:
        return False

    if graph[a][b] == '-':
        # 방문 처리
        graph[a][b] = 'v'
        # 좌우 재귀 호출
        dfs1(a, b - 1)
        dfs1(a, b + 1)
        return True
    return False


def dfs2(a, b):
    # 방을 벗어나는 조건
    if a < 0 or a >= n or b < 0 or b >= m:
        return False

    if graph[a][b] == '|':
        # 방문 처리
        graph[a][b] = 'v'
        # 상하 재귀 호출
        dfs2(a - 1, b)
        dfs2(a + 1, b)
        return True
    return False


res = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == '-':
            if dfs1(i, j):
                res += 1
        elif graph[i][j] == '|':
            if dfs2(i, j):
                res += 1
        else:
            continue


print(res)


