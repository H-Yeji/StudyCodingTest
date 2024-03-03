n = int(input())
arr = []
for i in range(n):
    arr.append(input())

for i in range(n - 1):
    for j in range(i, n):
        # 길이확인
        if len(arr[j]) < len(arr[i]):
            arr[i], arr[j] = arr[j], arr[i]
        elif len(arr[i]) == len(arr[j]): # 길이가 같다면 숫자 비교
            resultA, resultB = 0, 0
            for k in range(len(arr[i])):
                if 'A' <= arr[i][k] <= 'Z':
                    continue
                else:
                    resultA += int(arr[i][k])
            for k in range(len(arr[j])):
                if 'A' <= arr[j][k] <= 'Z':
                    continue
                else:
                    resultB += int(arr[j][k])
            if resultA > resultB:
                arr[i], arr[j] = arr[j], arr[i]

            # 숫자가 같으면 사전순 비교
            if resultA == resultB:
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]


for i in range(n):
    print(arr[i])
