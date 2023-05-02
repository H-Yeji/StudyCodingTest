N, M, K = map(int, input().split())
numArray = list(map(int, input().split()))

#큰 수 법칙 알고리즘
numArray.sort() #오름차순 정렬
first = numArray[N - 1] #가장 큰 수
second = numArray[N - 2] #가장 작은 수
sum = 0

#(1) 단순한 방법
'''
while True:
    for i in range(K): #가장 큰 수 k번 더하기
        if M == 0:
            break
        sum += first #k번 first 더해주고 M값 감소
        M -= 1

    if M == 0:
        break
    sum += second #second 숫자 '한 번'만 더해주기
    M -= 1
'''

#(2) 답안

#가장 큰 수가 더해지는 횟수 계산
cnt = int(M / (K + 1) * K)
cnt += M % (K + 1)

sum += cnt * first
sum += (M - cnt) * second

#출력
print(sum)