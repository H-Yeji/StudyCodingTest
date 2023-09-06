def solution(n):
    answer = 0

    while n >= 10:
        answer += n % 10
        n //= 10
    answer += n
    return answer

n = int(input())
print(solution(n))

'''
# 다른사람 코드
def sum_digit(number):
    return sum([int(i) for i in str(number)])
'''

