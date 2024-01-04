import sys

n = int(sys.stdin.readline())
arrN = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
arrM = list(map(int, sys.stdin.readline().split()))


def binary_search(arrN, target, start, end):

    if start > end:
        return "no"
    mid = (start + end) // 2

    if arrN[mid] == target:
        return "yes"
    elif arrN[mid] > target:
        return binary_search(arrN, target, start, mid - 1)
    else:
        return binary_search(arrN, target, mid + 1, end)


arrN.sort()
for i in range(len(arrM)):
    result = binary_search(arrN, arrM[i], 0, n)
    print(result, end=" ")
