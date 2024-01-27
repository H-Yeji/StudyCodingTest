import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()
maxW = 0
j = n
for i in range(n):
    w = arr[i] * j
    maxW = max(w, maxW)
    j -= 1

print(maxW)
