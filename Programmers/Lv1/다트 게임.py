def solution(dart):
    des = []
    for i in range(len(dart)):
        if dart[i] == 'S' or dart[i] == 'D' or dart[i] == 'T':
            des.append(1)
            num = des[len(des) - 2]
            if dart[i] == 'S':
                des[len(des) - 2] = num
            elif dart[i] == 'D':
                des[len(des) - 2] = num * num
            else:
                des[len(des) - 2] = num * num * num
        elif dart[i] == '*' or dart[i] == '#':
            if dart[i] == '*':
                if i == 2: # 첫판에서 *인 경우
                    des[len(des) - 1] *= 2
                else:
                    des[len(des) - 1] *= 2
                    des[len(des) - 3] *= 2
            else:
                des[len(des) - 1] *= -1
        elif 0 <= int(dart[i]) <= 10:
            if int(dart[i]) == 0 and i != 0 and len(des) % 2 == 1:
                des[len(des) - 1] *= 10
                continue
            des.append(int(dart[i]))

    n, result = 0, 0
    for i in range(len(des)):
        if i % 2 == 0:
            n += des[i]
        else:
            n *= des[i]
            result += n
            n = 0
    return result


dart = "1D2S3T*"
print(solution(dart))
