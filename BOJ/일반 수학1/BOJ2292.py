n = int(input())

number = 1
honeycomb = 1

while n > number: # 주어진 숫자가 더 크다면
    number += (6 * honeycomb) # 해당 층이 아니므로 다음 층으로
    honeycomb += 1

print(honeycomb)