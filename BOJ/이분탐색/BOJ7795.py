n = int(input())


def binary_search(setA, target, start, end):

    result = -1
    while start <= end:
        mid = (start + end) // 2
        if setA[mid] > target:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result


for i in range(n):
    a, b = map(int, input().split())
    setA = list(map(int, input().split()))
    setB = list(map(int, input().split()))
    setA.sort()
    setB.sort()

    result = 0
    for target in setB:
        returnNum = binary_search(setA, target, 0, a - 1)
        result += (a - returnNum - 1)
    print(result)
