import sys
input = sys.stdin.readline

s = input().strip()
stack = []
result = 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append('(')
    else: # 닫힌 괄호
        stack.pop()
        if s[i - 1] == '(': # 레이저인 경우 
            print(len(stack))
            result += len(stack)
        else:
            result += 1 # 막대의 끝인 경우 
        
print(result)


