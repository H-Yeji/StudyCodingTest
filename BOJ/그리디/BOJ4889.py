import sys
input = sys.stdin.readline

idx = 0
while True:
    s = input()
    idx += 1
    if '-' in s:
        break

    balance = 0
    operation = 0
    for char in s:
        if char == '{':
            balance += 1
        elif char == '}':
            balance -= 1

        if balance < 0:
            operation += 1
            balance = 1

    operation += balance // 2
    print(idx, end="")
    print(".", operation)

