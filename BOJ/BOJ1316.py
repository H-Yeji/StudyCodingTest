n = int(input())
sum = 0

for i in range(n):
    word = input()
    sum += list(word) == sorted(word, key=word.find)

print(sum)