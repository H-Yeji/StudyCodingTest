import sys
sys.setrecursionlimit(10 ** 6) #재귀 허용 깊이를 수동으로 늘려줌 (런타임 에러 방지)

r, c = map(int, input().split())
graph = []
for i in range(r):
    graph.append(list(map(str, input())))


def dfs(a, b):
    if a < 0 or a >= r or b < 0 or b >= c or graph[a][b] == '#':
        return 0

    if graph[a][b] == 'o':
        global sheep_count
        sheep_count += 1
    elif graph[a][b] == 'v':
        global wolf_count
        wolf_count += 1

    # 방문한 칸을 표시
    graph[a][b] = '#'

    # 상하좌우 이동
    dfs(a, b - 1)
    dfs(a, b + 1)
    dfs(a - 1, b)
    dfs(a + 1, b)


s, w = 0, 0
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'o' or graph[i][j] == 'v':
            sheep_count, wolf_count = 0, 0
            dfs(i, j)

            if sheep_count > wolf_count:
                wolf_count = 0
            elif sheep_count <= wolf_count:
                sheep_count = 0

            s += sheep_count
            w += wolf_count

print(s, w)
