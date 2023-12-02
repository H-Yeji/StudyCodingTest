arr = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

n = input()
m = (int(n[1]), ord(n[0]) - 96)

count = 0
for i in arr:
    result = tuple(sum(elem) for elem in zip(i, m))
    if (result[0] > 0) and (result[0] < 9):
        if (result[1] > 0) and (result[1] < 9):
            count += 1

print(count)
