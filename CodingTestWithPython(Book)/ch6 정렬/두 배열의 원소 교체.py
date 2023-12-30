n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))


for i in range(k):
    a = sorted(a)
    b = sorted(b, reverse=True)
    a[0], b[0] = b[0], a[0]


print(sum(a))
