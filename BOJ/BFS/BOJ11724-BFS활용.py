from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
visited[1] = True

q = deque([1])
cnt = 0
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if not visited[next_node]:
            visited[next_node] = True
            q.append(next_node)

    if len(q) == 0:
        cnt += 1
        for i in range(2, n + 1):
            if not visited[i]:
                q.append(i)
                break

print(cnt)
