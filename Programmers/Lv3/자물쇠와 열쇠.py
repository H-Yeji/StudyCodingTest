def rotate_key_90(key):
    n = len(key)
    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            result[j][n - i - 1] = key[i][j]
    return result


def check(new_lock):
    n = len(new_lock) // 3
    for i in range(n, n * 2):
        for j in range(n, n * 2):
            if new_lock[i][j] != 1:
                return False

    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]  # 가로 세로 3배씩 자물쇠 늘리기

    # 중앙 부분에 좌물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    # 4방향 모두 진행
    for rotation in range(4):
        key = rotate_key_90(key)

        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]

                if check(new_lock):
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False


print(solution([[0, 1, 0], [0, 1, 1], [0, 0, 0]], [[1, 1, 1], [1, 1, 1], [1, 1, 1]]))
