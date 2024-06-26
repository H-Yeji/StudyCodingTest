from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    q = deque([start])
    # 현재 노드 방문처리
    visited[start] = True
    
    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 하나씩 원소 뽑아 출력
        v = q.popleft()
        print(v, end=" ")

        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현 (2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
# 각 노드가 방문된 정보를 리스트 자료형으로 표현 (1차원 리스트)
visited = [False] * 9
# 정의된 DFS 함수 호출
bfs(graph, 1, visited)
