import sys
input = sys.stdin.readline

dic = {}
flag = 0
n = int(input())
for i in range(n):
    key, value = map(str, input().split())

    if key in dic:
        num = int(dic[key])
        dic[key] = int(value) + num
    else:
        dic[key] = int(value)

for key in dic:
    if dic[key] == 5:
        print('YES')
        flag = 1
        break
if flag == 0:
    print('NO')
