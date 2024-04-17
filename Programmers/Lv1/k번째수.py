def solution (arr, commands):
    result = []
    for command in commands:
        slice_arr = []
        i = command[0]
        j = command[1]
        k = command[2]

        slice_arr = arr[i - 1:j]
        slice_arr.sort()
        c = slice_arr[k - 1]
        result.append(c)

    return result


arr = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(arr, commands))
