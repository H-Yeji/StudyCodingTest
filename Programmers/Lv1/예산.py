import sys
input = sys.stdin.readline


def solution(d, budget):
    d.sort()
    cnt, sumNum = 0, 0
    for i in d:
        sumNum += i
        if budget < sumNum:
            break
        cnt += 1

    return cnt


d = list(map(int, input().split()))
budget = int(input())
print(solution(d, budget))
