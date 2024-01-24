def solution(nums):
    answer = 0
    half_nums = len(nums) // 2
    nums = set(nums)
    
    if len(nums) < half_nums:
        answer = len(nums)
    else:
        answer = half_nums
    return answer