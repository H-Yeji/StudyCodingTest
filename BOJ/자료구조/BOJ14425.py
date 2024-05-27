import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}
for i in range(n):
    s = input().strip() # 공백 제거
    dic[s] = 1

result = 0
for i in range(m):
    t = input().strip()
    if t in dic:
        result += dic[t]
print(result)