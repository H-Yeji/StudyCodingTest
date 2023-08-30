while True:
    a, b, c = map(int, input().split())
    if (a == 0) & (b == 0) & (c == 0):
        break

    M = max(a, b, c)
    m = min(a, b, c)
    if (sum([a, b, c]) - (M + m)) > (M - m):
        if (a == b) and (b == c):
            print("Equilateral")
        elif (a != b) and (b != c) and (c != a):
            print("Scalene")
        else:
            print("Isosceles")
    else:
        print("Invalid")
