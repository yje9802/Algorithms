import math

def ceil_sqrt(n):
    r = math.isqrt(n)
    return r if r * r == n else r + 1

def solution(r1, r2):
    answer = 0
    
    r1sq = r1 * r1 # 반지름 제곱
    r2sq = r2 * r2
    
    # 우선 1사분면만 카운트
    for x in range(1, r2+1):
        # 바깥원 내부: y^2 <= r2^2 - x^2
        y_max = math.isqrt(r2sq - x * x)
        # 안쪽원 외부: y^2 >= r1^2 - x^2
        t = r1sq - x * x
        
        if t <= 0:
            y_min = 0
        else:
            y_min = ceil_sqrt(t)
        
        # 축 제외(y>=1)
        y_low = max(1, y_min)

        if y_max >= y_low:
            answer += (y_max - y_low + 1)
    
    answer = answer * 4 + 4 * (r2 - r1 + 1)
    return answer