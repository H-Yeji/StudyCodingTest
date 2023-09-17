n = int(input())

list_x = []
list_y = []
for _ in range(n):
    a, b = map(int, input().split())
    list_x.append(a)
    list_y.append(b)

if n > 1:
    x = max(list_x) - min(list_x)
    y = max(list_y) - min(list_y)
    print(x * y)
else:
    print(0)
