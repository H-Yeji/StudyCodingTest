n = int(input())
arr = []
while n != 0:
    arr.append(n % 10)
    n = n // 10
arr.sort(reverse=True)
#print(''.join(arr))
print(''.join(map(str, arr)))
