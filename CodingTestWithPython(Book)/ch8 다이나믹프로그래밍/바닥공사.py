'''
설명)
바닥 타일을 n=1일 때 부터 그려보면
n=3일 때 부터 덮개로 덮는 부분이 중복되어 반복되는 것을 확인할 수 있음
중복되기 때문에 그 부분을 이용해 점화식으로 표현해주면 됨
'''

import sys

n = int(sys.stdin.readline())

d = [0]
d.append(1)
d.append(3)
for i in range(3, n + 1):
    d.append((d[i - 1] + d[i - 2] * 2) % 796796)


print(d[n])
