s = input()
cnt0, cnt1, flag = 0, 0, 0

for i in s:
    # 첫번째 원소
    if flag == 0:
        n = i
        flag += 1
        continue

    # 두번째 원소부터
    if n != i:
        if n == '0':
            cnt0 += 1
            n = i
        else:
            cnt1 += 1
            n = i
# 마지막 원소
if s[len(s) - 1] == '0':
    cnt0 += 1
else:
    cnt1 += 1

print(min(cnt0, cnt1))
