from itertools import combinations

def solution(nums):
    answer = 0

    for n in combinations(nums, 3):
        num = sum(n)
        for i in range(2, num):
            if num % i == 0:
                break
        else:
             answer += 1   

    return answer