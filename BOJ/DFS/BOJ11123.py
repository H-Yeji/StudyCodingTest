import sys
sys.setrecursionlimit(10 ** 6) #재귀 허용 깊이를 수동으로 늘려줌 (런타임 에러 방지)


def dfs(i, j, a, b):
    if i < 0 or i >= a or j < 0 or j >= b:
        return False

    if graph[i][j] == '#':
        graph[i][j] = '.'
        dfs(i, j - 1, a, b)
        dfs(i, j + 1, a, b)
        dfs(i - 1, j, a, b)
        dfs(i + 1, j, a, b)
        return True
    return False


n = int(input())
for _ in range(n):
    res = 0
    a, b = map(int, input().split())
    graph = [list(input()) for _ in range(a)]

    for i in range(a):
        for j in range(b):
            if graph[i][j] == '#':
                if dfs(i, j, a, b):
                    res += 1

    print(res)
