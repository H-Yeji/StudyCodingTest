n = int(input())
n_list = list(map(int, str(n)))

i = len(n_list) // 2
sumL, sumR = 0, 0

for j in range(i):
    sumL += n_list[j]
    sumR += n_list[j + i]

if sumL == sumR:
    print("LUCKY")
else:
    print("READY")
