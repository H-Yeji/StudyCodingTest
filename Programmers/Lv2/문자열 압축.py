def solution(s):
    answer = len(s)
    # 1개부터 len(s)//2 개까지 step별로 반복
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        word = s[0:step] # 비교할 단어
        cnt = 1

        for j in range(step, len(s), step):
            if word == s[j:j+step]:
                cnt += 1
            else: # 비교 단어와 다르면
                compressed += str(cnt) + word if cnt >= 2 else word # 압축 진행
                word = s[j:j+step] # 다음 단어 = 비교 당한 단어 저장 (초기화)
                cnt = 1

        # 남은 문자열 처리
        compressed += str(cnt) + word if cnt >= 2 else word
        # 압축한 문자열 길이 비교
        answer = min(answer, len(compressed))
    return answer


s = input()
print(solution(s))
