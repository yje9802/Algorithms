from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    
    nums = set()
    for i in range(1, len(numbers)+1):
        for p in permutations(numbers, i):
            n = int(''.join(p))
            nums.add(n)
    
    for num in nums:
        if is_prime(num):
            answer += 1
    return answer