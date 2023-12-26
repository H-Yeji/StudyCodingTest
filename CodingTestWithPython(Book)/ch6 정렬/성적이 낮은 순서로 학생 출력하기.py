n = int(input())
arr = []
for i in range(n):
    name, grade = map(str, input().split())
    arr.append((name, int(grade))) # 튜플로 리스트에 append


def setting(data):
    return data[1] # 점수 추출


result = sorted(arr, key=setting) # 점수로 정렬
for i in range(len(result)):
    print(result[i][0], end=" ") # 정렬된 result에서 이름만 출력 


# arr = sorted(arr, key lambda student: studnt[1] 와 같음
# for student in arr:
#   print(student[0], end=" ")와 같음
