import math

def check(number):
    if len(number) == 1 or '1' not in number or '0' not in number:
        return True
    
    root_idx = len(number) // 2 # 가운데 노드가 루트 노드
    if number[root_idx] == '0':
        return False
    
    return check(number[:root_idx]) and check(number[root_idx+1:])

def solution(numbers):
    answer = []
    for number in numbers:
        bin_number = str(bin(number)[2:])
        # 포화 이진트리의 노드 개수는 반드시 2^n - 1
        digit = 2 ** (int(math.log(len(bin_number), 2)) + 1) - 1
        if len(bin_number) < digit:
            bin_number = '0'*(digit - len(bin_number)) + bin_number

        result = 1 if check(bin_number) else 0
        answer.append(result)
        
    return answer