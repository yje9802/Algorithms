def solution(n):
    answer = -1
    
    sqrt = n**(1/2)
    if int(sqrt)**2 == (sqrt)**2:
        answer = (int(sqrt) + 1)**2
    return answer