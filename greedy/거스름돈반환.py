N = 1260
cnt = 0

coin_type = [500, 100, 50, 10]

for coin in coin_type:
    cnt += N // coin
    N %= coin

print(cnt)