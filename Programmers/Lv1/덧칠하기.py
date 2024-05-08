def solution(n, m, sections):
    cnt = 0
    painted = [0] * n
    for section in sections:
        if painted[section - 1] == 0 and section <= n - m + 1:
            painted[section-1:section-1+m] = [1] * m
            cnt += 1
        elif painted[section - 1] == 0 and section > n - m + 1:
            painted[-m:] = [1] * m
            cnt += 1

    return cnt


n, m = 4, 1
sections = [1, 2, 3, 4]
print(solution(n, m, sections))
