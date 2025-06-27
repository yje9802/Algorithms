def solution(numbers):
    s_numbers = [str(n) for n in numbers] # 정수 전부 문자열 변환
    
    s_numbers.sort(key=lambda x: x*4, reverse=True)
    
    answer = ''.join(s_numbers)
    
    return '0' if answer[0] == '0' else answer