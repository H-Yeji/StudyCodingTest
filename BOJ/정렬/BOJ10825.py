import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    name, kor, eng, math = map(str, sys.stdin.readline().split())
    arr.append((name, int(kor), int(eng), int(math)))


result = sorted(arr, key=lambda x: (-x[1], x[2], -x[3], x[0]))
for student in result:
    print(student[0])

