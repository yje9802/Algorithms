import math

def find_row_and_column(quotient, mod, n):
    if mod == 0:
        x = quotient-1
        if quotient % 2 == 0:
            y = 0
        else:
            y = n - 1
    else:
        x = quotient
        if quotient % 2 == 0:
            y = mod - 1
        else:
            y = n - mod
    return (x, y)

def solution(n, w, num):
    answer = 0
    h = math.ceil(n / w) # 세로로 쌓이는 상자의 개수
    
    quotient = num // w # num의 몫
    mod = num % w # num의 나머지
    x, y = find_row_and_column(quotient, mod, w) # num이 위치하는 행, 열
    
    last_x, last_y = find_row_and_column(n//w, n%w, w) # 마지막 상자의 행, 열
    if last_x % 2 == 0:
        if last_y < y:
            answer = h - x - 1
        else:
            answer = h - x
    else:
        if last_y <= y:
            answer = h - x
        else:
            answer = h - x - 1
    
    return answer