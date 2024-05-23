import heapq 
import sys
input = sys.stdin.readline

n = int(input())
q = [] # heap 리스트 
for i in range(n):
    m = int(input())
    if m == 0: 
        if len(q) == 0:
            print("ouput: ", '0')
        else:
            print("ouput: ", -heapq.heappop(q))
    else:
        heapq.heappush(q, -m)
