def solution(k, m, score):
    sumBox = 0

    score.sort(reverse=True)
    for i in range(len(score)):
        if (i + 1) % m == 0:
            sumBox += score[i] * m

    return sumBox

k, m = map(int, input().split())
score = list(map(int, input().split()))
print(solution(k, m, score))

'''
    #시간 초과 
    def solution(k, m, score):
    sumBox = 0

    score.sort(reverse=True)
    n = len(score) // m
    for _ in range(n):
        list_m = []
        for i in range(m):
            list_m.append(score[0])
            score.remove(score[0])
        sumBox += m * list_m[m - 1]

    return sumBox'''

