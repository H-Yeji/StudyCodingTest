from collections import deque
import sys
input = sys.stdin.readline


def empty(q):
    if len(q) == 0:
        return 1
    else:
        return 0


n = int(input())
q = deque()
for i in range(n):
    command = input().split()
    if command[0] == 'push_front':
        q.appendleft(command[1])
    elif command[0] == 'push_back':
        q.append(command[1])
    elif command[0] == 'pop_front':
        if empty(q) == 1:
            print(-1)
        else:
            print(q.popleft())
    elif command[0] == 'pop_back':
        if empty(q) == 1:
            print(-1)
        else:
            print(q.pop())
    elif command[0] == 'size':
        print(len(q))
    elif command[0] == 'empty':
        print(empty(q))
    elif command[0] == 'front':
        if empty(q) == 1:
            print(-1)
        else:
            print(q[0])
    elif command[0] == 'back':
        if empty(q) == 1:
            print(-1)
        else:
            print(q[len(q) - 1])
