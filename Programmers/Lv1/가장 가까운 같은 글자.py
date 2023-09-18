def solution(s):
    answer = []
    answer.append(-1)
    for i in range(1, len(s)):
        cnt = 0
        for j in range(i - 1, -1, -1):
            if s[i] == s[j]:
                cnt += 1
                answer.append(cnt)
                break
            else:
                cnt += 1
        if (cnt == i) & (s[i] != s[j]):
            answer.append(-1)

    return answer

s = input()
print(solution(s))

