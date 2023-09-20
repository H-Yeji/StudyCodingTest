arr = []
sumN = 0
for _ in range(5):
    n = int(input())
    sumN += n
    arr.append(n)

arr.sort()
print(int(sumN / 5))
print(arr[2])
