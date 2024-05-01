def division(n):
    for i in range(1, int(n ** (1/2)) + 1):
        if n % i == 0 and i != 1 and i != n:
            return False
    return True


def solution(nums):
    cnt = 0
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                num = nums[i] + nums[j] + nums[k]
                ret = division(num)
                if ret == 1:
                    cnt += 1
    return cnt


nums = [1,2,7,6,4]
print(solution(nums))