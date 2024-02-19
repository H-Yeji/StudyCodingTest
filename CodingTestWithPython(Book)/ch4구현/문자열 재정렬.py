sentence = input()
letter_list = []
num_list = []

for i in range(len(sentence)):
    if 'A' <= sentence[i] <= 'Z':
        letter_list.append(sentence[i])
    else:
        num_list.append(int(sentence[i])) # 숫자로 저장

# 공백없이 letter 리스트를 받아오고 num리스트의 합을 문자로 가져오기
result = ''.join(sorted(letter_list)) + str(sum(num_list))
print(result)
