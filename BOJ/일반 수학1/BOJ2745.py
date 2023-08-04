a, b = input().split()
arr = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

a = a[::-1] #리스트 역순으로
sum = 0

for i, n in enumerate(a):
    sum += (arr.index(n))*(int(b)**i)

print(sum)