import sys

sys.setrecursionlimit(10 ** 6)  # 재귀 허용 깊이를 수동으로 늘려줌 (런타임 에러 방지)
input = sys.stdin.readline


def dfs(i, j):
    if i < 0 or i >= h or j < 0 or j >= w:
        return False

    if arr[i][j] == 1:
        arr[i][j] = 0
        # 상하좌우
        dfs(i, j - 1)
        dfs(i, j + 1)
        dfs(i - 1, j)
        dfs(i + 1, j)
        # 대각선
        dfs(i - 1, j - 1)
        dfs(i - 1, j + 1)
        dfs(i + 1, j - 1)
        dfs(i + 1, j + 1)
        return True
    return False


while True:
    result = 0
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    arr = []
    for _ in range(h):
        arr.append(list(map(int, input().split())))

    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                if dfs(i, j):
                    result += 1
            else:
                continue
    print(result)
