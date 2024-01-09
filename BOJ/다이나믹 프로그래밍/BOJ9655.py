import sys
n = int(sys.stdin.readline())

d = []
while n > 0:
    if n >= 3:
        d.append(3)
        n -= 3
    else:
        d.append(1)
        n -= 1


if len(d) % 2 == 0:
    print("CY")
else:
    print("SK")

