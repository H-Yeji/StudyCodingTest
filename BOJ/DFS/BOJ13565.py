import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    row = input().strip()
    graph.append(list(map(int, row)))


def dfs(i, j):
    if i < 0 or i >= n or j < 0 or j >= m:
        return False

    if graph[i][j] == 0:
        graph[i][j] = 1

        if i == n - 1:
            return True
        if dfs(i, j - 1) or dfs(i, j + 1) or dfs(i - 1, j) or dfs(i + 1, j):
            return True
    return False


flag = 0
for j in range(m):
    if graph[0][j] == 0:
        if dfs(0, j):
            print("YES")
            flag = 1
            break

if flag == 0:
    print("NO")
