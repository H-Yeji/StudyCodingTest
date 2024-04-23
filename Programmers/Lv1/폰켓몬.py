def solution(nums):
    n = int(len(nums) / 2)
    nums = list(set(nums))

    if len(nums) <= n:
        result = len(nums)
    else:
        result = n
    return result


nums = [3,1,2,3]
print(solution(nums))
