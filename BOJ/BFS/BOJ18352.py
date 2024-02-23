# BOJ18352 BFS 풀이
from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


distance = [-1] * (n + 1)
distance[x] = 0 # 출발 도시까지 거리 0으로 설정

q = deque([x])
while q:
    now = q.popleft()
    # now 도시에 연결되어 있는 도시들을 순서대로 방문
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)


check = False
for i in range(1, n + 1):
    if distance[i2] == k:
        print(i)
        check = True

if not check:
    print(-1)
