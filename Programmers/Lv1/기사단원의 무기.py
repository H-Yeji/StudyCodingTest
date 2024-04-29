# 약수 구하기
def divisor(number): # if number = 16
    result = []
    for i in range(1, int(number**(1/2)) + 1):
        if number % i == 0:
            result.append(i)
            if i < number//i:
                result.append(number//i) # [1, 16, 2, 8, 4]
        result.sort()
    return result


def solution(number, limit, power):
    result = []
    for i in range(1, number+1):
        div = divisor(i)
        result.append(len(div))

    for i in range(len(result)):
        if result[i] > limit:
            result[i] = power

    Sum = sum(result)
    return Sum


number = 5
limit = 3
power = 2
print(solution(number, limit, power))
