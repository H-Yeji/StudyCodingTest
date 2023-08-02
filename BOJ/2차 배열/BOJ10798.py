A = []
max_len = 0
for i in range(5):
    row = list(input())
    A.append(row)
    if len(row) > max_len:
        max_len = len(row)

for i in range(max_len):
    for j in range(5):
        if i < len(A[j]):
            print(A[j][i], end="")