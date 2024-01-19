import sys

input = sys.stdin.readline
inf = int(1e9)

# 그래프 생성
node, edge = map(int, input().split())
graph = [[inf] * (node + 1) for _ in range(node + 1)]
for i in range(1, node + 1):
    for j in range(1, node + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(edge):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

# 플로이드 워셜 알고리즘
for n in range(1, node + 1):
    for i in range(1, node + 1):
        for j in range(1, node + 1):
            graph[i][j] = min(graph[i][j], graph[i][n] + graph[n][j])


distance = graph[1][k] + graph[k][x]
if distance >= inf:
    print("-1")
else:
    print(distance)
