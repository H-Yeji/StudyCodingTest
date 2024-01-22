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
    # 시작 도시와 도착 도시를 연결하는 노선이 하나가 아닐 수 있으므로 최소인 것 사용
    graph[a][b] = min(graph[a][b], c)


# 플로이드 워셜 알고리즘 수행
for node in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][node] + graph[node][j])


for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == inf:
            print(0, end=" ") # i에서 j로 갈 수 없는 경우 == inf인경우 0출력
        else:
            print(graph[i][j], end=" ")
    print()
