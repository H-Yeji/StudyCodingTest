arr = sorted(list(map(int, input().split())))

if (arr[0] + arr[1]) > arr[2]:
    print(sum(arr))
else:
    n = arr[0] + arr[1] - 1
    print(arr[0] + arr[1] + n)
