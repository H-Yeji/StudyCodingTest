import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}
for i in range(n):
    team = input().strip()
    cnt = int(input())

    for j in range(cnt):
        member = input().strip()
        dic[member] = team #member이름을 key로, 팀을 value로 잡기 

for i in range(m):
    quiz_name = input().strip()
    tf = int(input())
    if tf == 1:
        print(dic[quiz_name]) # member의 팀 출력
    else:
        result = [j for j, k in dic.items() if k == quiz_name] # value로 key 얻기
        result.sort()
        print(*result, sep='\n')

