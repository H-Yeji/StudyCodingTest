import sys

input = sys.stdin.readline
inf = int(1e9)

n, m = map(int, input().split())

# 그래프 생성
graph = [[inf] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


# 플로이드 워셜 알고리즘 수행
for node in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][node] + graph[node][j])


graph = graph[1:] # 첫번째 행 삭제
graph = [sublist[1:] for sublist in graph] # 첫번째 열 삭제

result = inf
num = 0
for i, value in enumerate(graph):
    if result > sum(value):
        result = sum(value)
        num = i

print(num + 1)
