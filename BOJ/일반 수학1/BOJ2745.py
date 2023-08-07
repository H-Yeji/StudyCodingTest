a, b = input().split()
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

a = a[::-1] #리스트 역순으로
result = 0

for i, n in enumerate(a):
    result += (arr.index(n))*(int(b)**i)

print(result)