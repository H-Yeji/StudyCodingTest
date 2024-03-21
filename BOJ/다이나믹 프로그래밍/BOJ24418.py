'''import sys
input = sys.stdin.readline

cntA, cntB = 0, 0
def matrix_path_rec(m, i, j):
    global cntA
    if i < 0 or j < 0:
        cntA += 1
        return 0
    else:
        return m[i][j] + (max(matrix_path_rec(m, i - 1, j), matrix_path_rec(m, i, j - 1)))

def matrix_path(m, n):
    global cntB
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            cntB += 1
            dp[i][j] = m[i - 1][j - 1] + max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][n]


n = int(input())
m = []
for i in range(n):
    m.append(list(map(int, input().split())))


matrix_path_rec(m, n - 1, n - 1)
matrix_path(m, n)
print(cntA, cntB)
'''

from math import factorial

n = int(input())
m = [list(map(int, input().split())) for _ in range(n)]
print(factorial(2 * n) // (factorial(n) ** 2), n ** 2)