import sys
input = sys.stdin.readline


def solution(n, arr1, arr2):
    # 10진수 > 2진수 변환
    arr1_bin, arr2_bin = [], []
    for i in range(n):
        b1 = format(arr1[i], 'b')
        b2 = format(arr2[i], 'b')

        # arr1
        if len(b1) < n:
            b1 = '0' * (n - len(b1)) + b1
            arr1_bin.append(b1)
        else:
            arr1_bin.append(b1)
        # arr2
        if len(b2) < n:
            b2 = '0' * (n - len(b2)) + b2
            arr2_bin.append(b2)
        else:
            arr2_bin.append(b2)

    # 합치기
    result_s = []
    for i in range(n):
        num = int(arr1_bin[i]) + int(arr2_bin[i])
        s = str(num)
        if len(s) < n:
            s = '0' * (n - len(s)) + s
        result_s.append(s)

    result = []
    for i in result_s:
        s = str(i)
        ss = ''
        for j in range(len(s)):
            if s[j] == '0':
                ss = ss + ' '
            else:
                ss = ss + '#'
        result.append(ss)
    return result


'''n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]'''
n = 6
arr1 = [46, 33, 33, 22, 31, 50]
arr2 = [27,56, 19, 14, 14, 10]
print(solution(n, arr1, arr2))

