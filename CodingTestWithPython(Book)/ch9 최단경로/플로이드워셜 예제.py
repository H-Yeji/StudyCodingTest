import sys

input = sys.stdin.readline
inf = int(1e9)

n = int(input())
m = int(input())

# 그래프 생성
graph = [[inf] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c


# 플로이드 워셜 알고리즘 수행
for node in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][node] + graph[node][j])


for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == inf:
            print("infinity", end=" ")
        else:
            print(graph[i][j], end=" ")
    print()
