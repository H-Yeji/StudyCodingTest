import sys
n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    m = int(sys.stdin.readline())
    arr.append(m)
arrSort = sorted(arr)
for i in arrSort:
    print(i)
