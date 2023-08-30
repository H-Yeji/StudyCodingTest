def solution(name, yearning, photo):
    dic = dict(zip(name, yearning))
    answer = []

    for i in range(len(photo)):
        n = 0
        for j in photo[i]:
            if j in dic.keys():
                n += dic[j]
        answer.append(n)
    return answer

name = list(map(str, input().split()))
yearning = list(map(int, input().split()))
photo = [list(map(str, input().split())) for _ in range(3)]
print(solution(name, yearning, photo))
