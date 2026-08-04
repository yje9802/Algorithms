from math import lcm

def solution(signals):
    answer = -1
    
    # 각 신호등의 반복 주기의 최소공배수 -> 확인해봐야할 최대 시간
    total_period = 1
    for G, Y, R in signals:
        period = G + Y + R
        total_period = lcm(total_period, period)
    
    for time in range(1, total_period+1):
        all_yellow = True
        
        for G, Y, R in signals:
            period = G + Y + R
            position = (time - 1) % period # 현재 색깔
            if not (G <= position < G + Y): # 노란불이 아님
                all_yellow = False
                break
        if all_yellow:
            return time
    return answer