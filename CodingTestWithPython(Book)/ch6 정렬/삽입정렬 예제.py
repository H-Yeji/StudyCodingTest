arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(arr)):
    for j in range(i, 0, -1): # i부터 1까지 1씩 감소하면서 반복
        if arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j] # 스와프
        else:
            break

print(arr)
