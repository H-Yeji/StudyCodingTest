def solution(k, score):
    hof, result = [], []
    check = 0
    for i in score:
        # k개가 명예의 전당에 채워지지 않았으면 채워넣기
        if check < k:
            hof.append(i)
            hof.sort(reverse=True)
            result.append(hof[len(hof) - 1])

            check += 1
            continue

        # k개가 명예의 전당에 모두 채워진 후부터는 비교해서 제외시키기
        hof.append(i)
        hof.sort(reverse=True)
        del hof[k]
        result.append(hof[len(hof) - 1])

    return result


k = 4
score = [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]
print(solution(k, score))
