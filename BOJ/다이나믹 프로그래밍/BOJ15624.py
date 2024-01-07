n = int(input())

d = [0, 1]

for i in range(2, n + 1):
    # append를 활용해 동적할당 -> 크기를 미리 알 수 없을 때 효율적
    d.append((d[i - 1] + d[i - 2]) % 1000000007)


print(d[n])
