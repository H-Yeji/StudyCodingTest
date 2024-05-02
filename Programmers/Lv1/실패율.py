def solution(n, stages):
    # 실패율 구하기
    result = []
    stages.sort()
    for i in range(1, n + 1):
        if len(stages) == 0 or stages.count(i) == 0:
            result.append(0)
            continue
        else:
            result.append(stages.count(i) / len(stages))
            stages = [x for x in stages if x != i]

    # 실패율에 따른 내림차순 인덱스 구하기
    Index = []
    filter_result = result
    while len(result) != len(Index):
        Max = max(filter_result)
        for i in range(len(result)):
            if Max == result[i]:
                Index.append(i + 1)
        filter_result = [x for x in filter_result if x != Max]

    return Index


n = 5
stages = [4, 4, 4]
print(solution(n, stages))
