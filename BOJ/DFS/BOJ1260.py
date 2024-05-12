from collections import deque
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    graph[a].sort()
    graph[b].sort()
result_dfs = []
result_bfs = []


# dfs
def dfs(node):
    visited[node] = True
    result_dfs.append(node)
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node)


visited = [False] * (n + 1)
dfs(v)

# bfs
visited = [False] * (n + 1)
visited[v] = True
q = deque([v])
while q:
    now = q.popleft()
    result_bfs.append(now)
    for next_node in graph[now]:
        if not visited[next_node]:
            visited[next_node] = True
            q.append(next_node)

print(*result_dfs)
print(*result_bfs)
