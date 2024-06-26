# 재귀함수 - 종료조건
"""def recursive_function(i):
    if i == 10:
        return
    print(i, "번째 재귀함수에서", i+1, "번째 재귀함수를 호출.")
    recursive_function(i+1)
    print(i, "번째 재귀함수를 종료.")

recursive_function(1)"""


# 팩토리얼을 재귀함수로
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


result = factorial_recursive(5)
print(result)
