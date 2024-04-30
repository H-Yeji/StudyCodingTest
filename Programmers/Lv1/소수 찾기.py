def division(n):
    result = []
    for i in range(1, int(n ** (1/2)) + 1):
        if n % i == 0 and i != 1 and i != n:
            return False
    return True


def solution(n):
    cnt = 0
    for i in range(2, n + 1):
        ret = division(i)
        if ret == 1:
            cnt += 1
    return cnt


n = 5
print(solution(n))
