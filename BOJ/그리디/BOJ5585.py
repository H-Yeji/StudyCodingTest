N = int(input())
coin = [500, 100, 50, 10, 5, 1]
result = 0

n = 1000 - N
for money in coin:
    result += n // money
    n = n % money

print(result)
