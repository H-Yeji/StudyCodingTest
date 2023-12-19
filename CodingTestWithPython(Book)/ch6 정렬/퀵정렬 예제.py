arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(start, end):
    if start >= end:
        return
    pivot = start
    l = start + 1
    r = end

    while l <= r:
        # 피봇보다 큰 데이터를 찾을 때까지 반복
        while l <= end and arr[l] <= arr[pivot]:
            l += 1
        # 피봇보다 작은 데이터를 찾을 때까지 반복
        while r > start and arr[r] >= arr[pivot]:
            r -= 1
        if l > r: # 엇갈렸다면 작은 데이터와 피봇을 교체
            arr[r], arr[pivot] = arr[pivot], arr[r]
        else:
            arr[l], arr[r] = arr[r], arr[l]

    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각 정렬 수행
    quick_sort(start, r - 1)
    quick_sort(r + 1, end)


quick_sort(0, len(arr) - 1)
print(arr)
