n, s = map(int, input().split())
sumNum = 0

for i in range(1, n+1):
    if n % i == 0:
        sumNum += 1

        if s == sumNum:
            print(i)
            break

if sumNum < s:
    print("0")
