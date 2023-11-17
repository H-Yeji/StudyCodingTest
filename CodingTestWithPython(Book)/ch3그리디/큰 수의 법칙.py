N, M, K = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

result = 0
a = M // (K + 1)
b = M % (K + 1)

result += ((arr[0] * K) + (arr[1] * 1)) * a
result += (arr[0] * b)

print(result)
