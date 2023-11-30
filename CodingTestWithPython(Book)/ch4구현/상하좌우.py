N = int(input())
command = list(map(str, input().split()))
#좌표 초기화
x, y = 1, 1

for i in range(len(command)):
    if command[i] == 'L' and y != 1:
        y -= 1
    elif command[i] == 'R' and y != N:
        y += 1
    elif command[i] == 'U' and x != 1:
        x -= 1
    elif command[i] == 'D' and x != N:
        x += 1

print(x, y)
