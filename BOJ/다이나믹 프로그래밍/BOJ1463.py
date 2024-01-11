import sys

n = int(sys.stdin.readline())
d = []
d.append(0) # 0번째 원소 0으로 초기화
d.append(0) # 1번째 원소 0으로 초기화

for i in range(2, n + 1):
    # 앞 번호의 연산수에서 +1
    d.append(d[i - 1] + 1)

    if i % 2 == 0:
        d[i] = (min(d[i], d[i // 2] + 1))
    if i % 3 == 0:
        d[i] = (min(d[i], d[i // 3] + 1))


print(d[n])
