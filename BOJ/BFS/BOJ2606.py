from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

connected = [False] * (n + 1)

q = deque([1]) # 1번 컴퓨터에서 시작
connected[1] = True # 1번 컴퓨터 방문처리
while q:
    now = q.popleft()
    for next_computer in graph[now]:
        if not connected[next_computer]:
            connected[next_computer] = True
            q.append(next_computer)

cnt = 0
for i in range(2, n + 1):
    if connected[i]: # True의 갯수
        cnt += 1

print(cnt)
