def solution(numbers):
    numbers.sort()
    result = []
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            result.append(numbers[i] + numbers[j])
    result = list(set(result))
    result.sort()
    return result


numbers = [0, 0, 0, 3, 4]
print(solution(numbers))
