import sys
input = sys.stdin.readline


def solution(s, n):
    result = []
    for i in range(len(s)):
        # 대문자
        if 65 <= ord(s[i]) <= 90:
            if ord(s[i]) + n > 90:
                tmpNum = (ord(s[i]) + n) - 26
                result.append(chr(tmpNum))
            else:
                result.append(chr(ord(s[i]) + n))
        # 소문자
        elif 97 <= ord(s[i]) <= 122:
            if ord(s[i]) + n > 122:
                tmpNum = (ord(s[i]) + n) - 26
                result.append(chr(tmpNum))
            else:
                result.append(chr(ord(s[i]) + n))
        # 공백
        else:
            result.append(" ")

    result = ''.join(result)
    return result


s = input().strip()
n = int(input())
print(solution(s, n))
