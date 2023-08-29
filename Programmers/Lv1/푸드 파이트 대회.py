def solution(food):
    answer = ''

    for i in range(1, len(food)):
        a = food[i] // 2
        answer += str(i) * a
    answer = answer + '0' + answer[::-1]
    return answer

food = list(map(int, input().split()))
print(solution(food))