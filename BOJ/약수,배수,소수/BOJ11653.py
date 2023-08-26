n = int(input())

'''for i in range(2, n+1):
    while True:
        if n % i == 0:
            print(i)
            n = n / i
        else:
            break

    if n == 1:
        break'''

for i in range(2, int(n ** 0.5)+2):
    while n % i == 0:
        print(i)
        n /= i
if n != 1:
    print(int(n))
