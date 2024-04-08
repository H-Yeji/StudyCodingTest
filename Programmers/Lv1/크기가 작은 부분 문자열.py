import sys
input = sys.stdin.readline


def solution(t, p):
    t_length, p_length = len(t), len(p)
    p_int = int(p)

    cnt = 0
    for i in range(len(t)):
        if t_length - p_length >= i:
            checkStr = t[i:i + p_length]
            if int(checkStr) <= p_int:
                cnt += 1
    return cnt


t = input().strip()
p = input().strip()
print(solution(t, p))
