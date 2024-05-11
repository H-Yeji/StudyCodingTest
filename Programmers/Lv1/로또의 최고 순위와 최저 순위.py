def solution(lottos, win_nums):
    cor, zero = 0, 0
    for lot in lottos:
        if lot == 0:
            zero += 1
            continue
        if win_nums.count(lot) == 1:
            cor += 1

    arr = [cor+zero, cor]
    result = []
    for i in arr:
        if i == 6:
            result.append(1)
        elif i == 5:
            result.append(2)
        elif i == 4:
            result.append(3)
        elif i == 3:
            result.append(4)
        elif i == 2:
            result.append(5)
        else:
            result.append(6)
    return result


lottos = [45, 4, 35, 20, 3, 9]
win_nums = [20, 9, 3, 45, 4, 35]
print(solution(lottos, win_nums))
