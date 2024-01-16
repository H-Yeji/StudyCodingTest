import heapq
import sys

input = sys.stdin.readline
inf = int(1e9)

n, m, c = map(int, input().split())
graph = [[] for i in range(n + 1)]
distance = [inf] * (n + 1)

for i in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(c)

city = 0
for i in range(0, n + 1):
    if distance[i] != inf and i != c:
        city += 1
    else:
        distance[i] = -1


# 시작도시와 연결되어있는 도시 개수와 총 걸리는 시간
print(city, max(distance))
