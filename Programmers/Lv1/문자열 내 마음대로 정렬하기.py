import sys
input = sys.stdin.readline


def solution(strings, n):
    # 사전순으로 정렬
    strings.sort()
    # n번째 문자로 정렬
    strings.sort(key=lambda x: x[n])
    return strings


strings = ["sun", "bed", "car"]
n = 1
print(solution(strings, n))
