def solution(a, b, n):
    answer = 0
    
    while n >= a and n >= 2:
        plus = (n // a) * b
        answer += plus
        
        n = plus + n % a
        
    return answer