import heapq
import sys

input = sys.stdin.readline
inf = int(1e9)

n, m, s = map(int, input().split())
graph = [[] for i in range(n + 1)]

# 그래프 생성
for i in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))


def dijkstra(start):
    q = []
    # 함수 호출마다 distance 초기화
    distance = [inf] * (n + 1)
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

    return distance


result = 0
for i in range(1, n + 1):
    go = dijkstra(i)
    back = dijkstra(s)
    result = max(result, go[s] + back[i])

print(result)
