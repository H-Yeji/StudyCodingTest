import sys
input = sys.stdin.readline

n, c = map(int, input().split())
arr = list(map(int, input().split()))

count = [0] * (max(arr) + 1)
order = {}
for i, num in enumerate(arr):
    count[num] += 1
    if num not in order:
        order[num] = i

dic = sorted(((num, cnt) for num, cnt in enumerate(count) if cnt > 0),
             key=lambda item: (-item[1], order.get(item[0])))

for num, _ in dic:
    for _ in range(count[num]):
        print(num, end=" ")
