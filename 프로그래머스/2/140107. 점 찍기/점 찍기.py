import math

def solution(k, d):
    answer = 0
    
    for x in range(0, d+1, k): # d 거리 내에서 가능한 x 좌표
        y = math.isqrt(d**2 - x**2)
        answer += y // k + 1
        
    return answer