def solution(a, b):
    week = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # day 계산
    n = a - 1
    day = 0
    for i in range(n):
        day += days[i]
    day += b
    # 요일 계산
    tmp = day % 7
    result = week[tmp]
    return result


a, b = 2, 3
print(solution(a, b))
