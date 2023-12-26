n = int(input())
arr = []
for i in range(n):
    m = int(input())
    arr.append(m)


arr.sort(reverse=True)
for i in arr:
    print(i, end=" ")


