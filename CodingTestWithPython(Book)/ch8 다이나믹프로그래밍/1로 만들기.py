n = int(input())
d = [0] * 30001

for i in range(2, n + 1): # 1이 되어야 하니까 연산은 2부터
    # 현재의 수에서 -1 하는 경우 (나누어 떨어지지 않으면 -1하고 이전 숫자 연산 그대로)
    d[i] = d[i - 1] + 1

    # 2, 3, 5로 나누어 떨어진 경우, 이미 초기화되어있는 연산수와 비교해서 작은 수 선택
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)


print(d[n])
