n = int(input())
line = 0
endNum = 0

while n > endNum:
    line += 1
    endNum += line

diff = endNum - n

if line % 2 == 0: #line이 짝수일 때
    top = line - diff
    bottom = diff + 1
else: #line이 홀수일 때
    top = diff + 1
    bottom = line - diff

print("%d/%d" % (top, bottom))