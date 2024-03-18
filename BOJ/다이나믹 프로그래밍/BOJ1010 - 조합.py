import sys
input = sys.stdin.readline


def cal(n, m):
    arrN = [i for i in range(1, n + 1)]
    arrM = [i for i in range(m, 0, -1)]

    resultA, resultB = 1, 1
    for i in range(n):
        resultA *= arrM[i]
        resultB *= arrN[i]
    return resultA, resultB


N = int(input())
for i in range(N):
    n, m = map(int, input().split())
    resultA, resultB = cal(n, m)
    print(resultA // resultB)
