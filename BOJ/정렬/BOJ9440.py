import sys
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))

    n = arr[0]
    if n == 0:
        break
    arrIn = arr[1:]
    # 정렬
    arrIn.sort()
    check_zero = arrIn.count(0) # 0의 개수 확인
    if 0 in arrIn:
        if check_zero == 1:
            arrIn[0], arrIn[2] = arrIn[2], arrIn[0]
        else:
            for i in range(2):
                arrIn[i], arrIn[i + check_zero] = arrIn[i + check_zero], arrIn[i]

    a, b = [], []
    flag = 0
    for i in range(len(arrIn)):
        if flag == 0:
            a.append(str(arrIn[i]))
            flag = 1
        else:
            b.append(str(arrIn[i]))
            flag = 0

    a, b = int(''.join(a)), int(''.join(b))
    print(a + b)
