while True:
    a = int(input())
    if a == -1: #종료 조건
        break

    arr = []
    for i in range(1, a):
        if a % i == 0:
            arr.append(i)

    #출력
    if sum(arr) == a:
        print("%d = " % a, end="")
        for j in range(len(arr)-1):
            print("%d + " % arr[j], end="")
        print(arr[-1])
    else:
        print("%d is NOT perfect." % a)
