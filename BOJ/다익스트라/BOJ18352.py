import heapq
import sys

input = sys.stdin.readline
inf = int(1e9)

n, m, k, c = map(int, input().split())
graph = [[] for i in range(n + 1)]
distance = [inf] * (n + 1)

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append((y, 1))


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

city = []
for i in range(1, n + 1):
    if distance[i] == k:
        city.append(i)

city.sort()
if len(city) == 0:
    print(-1)
else:
    print(*city, sep="\n")
