N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
for i in sorted(arr):
    print(i)
