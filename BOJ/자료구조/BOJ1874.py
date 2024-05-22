import sys
input = sys.stdin.readline

n = int(input())
num_list = []
for i in range(n):
    num_list.append(int(input()))

stack = []
result = []
idx = 0
for i in range(1, n + 1):
    if len(stack) == 0:
        stack.append(i)
        result.append("+")
        if stack[-1] != num_list[idx]:
            continue

    if stack[-1] < num_list[idx] and len(stack) != 0:
        stack.append(i)
        result.append("+")
    
    while stack[-1] == num_list[idx]:
            stack.pop()
            result.append("-")
            idx += 1
            if idx == n or len(stack) == 0:
                break
if len(result) == n * 2:
     for i in range(len(result)):
          print(result[i])
else:
     print("NO")
