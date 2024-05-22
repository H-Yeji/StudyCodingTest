import heapq
import sys
input = sys.stdin.readline

n = int(input())
q = []
for i in range(n):
    m = int(input())

    if m == 0:
        if len(q) == 0:
            print('0')
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q, m)
