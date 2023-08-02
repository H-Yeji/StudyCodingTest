A = []
max_row = -1
max_col = -1
max_num = -1

for i in range(9):
    row = list(map(int, input().split()))
    if max(row) > max_num:
        max_row = i #최댓값의 행
        max_col = row.index(max(row)) #최댓값의 열
        max_num = max(row) #최댓값


print(max_num)
print(max_row+1, max_col+1)
