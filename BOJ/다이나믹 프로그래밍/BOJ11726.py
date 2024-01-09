'''
설명 )
바닥 공사와 거의 같은 문제 (2x2 타일이 없을 뿐)
n=1일 때부터 시작해서 몇 개의 경우의 수가 있는지 계산하다보면
공통되어 계산되는 부분이 나타남 -> 점화식으로 표현하여 풀기
'''

import sys

n = int(sys.stdin.readline())

d = [0]
d.append(1)
d.append(2)

for i in range(3, n + 1):
    d.append((d[i - 1] + d[i - 2]) % 10007)


print(d[n])
