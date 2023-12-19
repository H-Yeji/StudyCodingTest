arr = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(arr):
    # 리스트가 하나 이하의 원소만 담고 있다면 종료ㅕ
    if len(arr) <= 1:
        return arr

    pivot = arr[0] # 첫번째 원소 = 피봇
    tail = arr[1:] # 피봇을 제외한 원소 리스트

    left_list = [x for x in tail if x <= pivot] # 분할된 왼쪽 리스트
    right_list = [x for x in tail if x > pivot] # 분할된 오른쪽 리스트

    # 분할 이후 왼쪽 리스트와 오른쪽 리스트에서 각각 정렬을 수행하고, 전체 리스트 반환 
    return quick_sort(left_list) + [pivot] + quick_sort(right_list)


print(quick_sort(arr))
