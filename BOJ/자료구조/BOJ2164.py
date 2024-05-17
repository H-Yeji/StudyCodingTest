from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
q = deque()
# 1~n까지 q에 넣기
for i in range(n):
    q.append(i + 1)

while 1:
    if len(q) == 1:
        break
    q.popleft() # 가장 위의 카드 바닥에 버리기
    m = q.popleft() # 그 다음카드 제일 아래로
    q.append(m)

print(q[0])

