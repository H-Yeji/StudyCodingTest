def check(b, arr):
    for i in range(len(b) - len(arr) - 1):
        # 해당 문자열이 연속됐는지 확인
        if b[i:i+len(arr)] == arr and b[i+len(arr):i+(len(arr)*2)] == arr:
            return True
    return False


def solution(babbling):
    arrays = ["aya", "ye", "woo", "ma"]
    cnt = 0
    for b in babbling:
        length = len(b)
        for arr in arrays:
            if b.count(arr) >= 2:
                Return = check(b, arr)
                if not Return:
                    length -= (len(arr) * b.count(arr))
            elif b.count(arr) == 1:
                length -= len(arr)
        if length == 0:
            cnt += 1

    return cnt


babbling = ["aya", "yee", "u", "maa"]
print(solution(babbling))
