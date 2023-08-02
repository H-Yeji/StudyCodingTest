arr = [[0] * 100 for _ in range(100)] #크기100인 2차배열 선언
a = []

n = int(input()) #색종이 수
for _ in range(n):
    x, y = list(map(int, input().split()))

    for i in range(x-1, x+10-1):
        for j in range(y-1, y+10-1):
            arr[i][j] = 1

result = 0
for i in arr:
    result += i.count(1) #1의 갯수 카운트
print(result)
