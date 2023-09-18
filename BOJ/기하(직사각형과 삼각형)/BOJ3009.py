x = []
y = []
for i in range(3):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

#x점 찾기
x.sort()
diff_x = max(x) - min(x)
if x.count(x[0]) == 1:
    print(max(x) - diff_x, end=" ")
elif x.count(x[2]) == 1:
    print(min(x) + diff_x, end=" ")

#y점 찾기
y.sort()
diff_y = max(y) - min(y)
if y.count(y[0]) == 1:
    print(max(y) - diff_y)
elif y.count(y[2]) == 1:
    print(min(y) + diff_y)
