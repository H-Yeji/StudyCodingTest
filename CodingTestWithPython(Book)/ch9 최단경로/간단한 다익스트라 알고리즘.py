import sys
input = sys.stdin.readline
inf = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]

visited = [False] * (n + 1)
distance = [inf] * (n + 1)

# 그래프 생성
for _ in range(m):
    startN, endN, edge = map(int, input().split())
    graph[startN].append((endN, edge))


# 방문하지 않은 노드 중 가장 최단 거리가 짧은 노드 번호 찾기
def get_smallest_node():
    minNum = inf
    index = 0
    for i in range(1, n + 1):
        if distance[i] < minNum and not visited[i]:
            index = i
    return index


def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost


dijkstra(start)

# 출력
for i in range(1, n + 1):
    if distance[i] == inf:
        print("INFINITY")
    else:
        print(distance[i])
