import sys
input = sys.stdin.readline


def solution(s):
    num_dic = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
               "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

    check = []
    result = []
    for i in s:
        # 문자이면
        if 'a' <= i <= 'z':
            check.append(i)

            # 하나 넣을 때마다 문장화
            change_s = ''.join(check)
            for key, value in num_dic.items():
                if key == change_s:
                    result.append(str(value))
                    check = [] # 빈것으로 초기화

        else:
            result.append(i)

    result = int(''.join(result))
    return result


s = input().strip()
print(solution(s))
