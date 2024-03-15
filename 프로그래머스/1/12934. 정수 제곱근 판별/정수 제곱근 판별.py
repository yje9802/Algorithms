def solution(n):
    answer = -1
    
    if int(n**(1/2))**2 == (n**(1/2))**2:
        answer = (int(n**(1/2)) + 1)**2
    return answer