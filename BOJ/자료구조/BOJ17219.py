import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}
for i in range(n):
    domain, pwd = map(str, input().split())
    dic[domain] = pwd
for i in range(m):
    find_key = input().strip()
    print(dic[find_key])
