n = int(input())
coin = [500, 100, 50, 10]
result = 0

for money in coin:
    result += n // money
    n = n % money

print(result)
