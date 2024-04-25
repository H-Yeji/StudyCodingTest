def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    f, s, t = 0, 0, 0
    cnt_f, cnt_s, cnt_t = 0, 0, 0
    for i in range(len(answers)):
        # first student
        if first[f] == answers[i]:
            cnt_f += 1
        f += 1
        if f == len(first):
            f = 0

        # second student
        if second[s] == answers[i]:
            cnt_s += 1
        s += 1
        if s == len(second):
            s = 0

        # third student
        if third[t] == answers[i]:
            cnt_t += 1
        t += 1
        if t == len(third):
            t = 0

    check, result = [0] * 3, []
    check[0], check[1], check[2] = cnt_f, cnt_s, cnt_t
    Max = max(check)
    for i in range(len(check)):
        if Max == check[i]:
            result.append(i + 1)

    return result


answers = [1, 2, 3, 4, 5]
print(solution(answers))
