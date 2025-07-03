def get_divisors(n):
    divisors = []
    for i in range(1, int(n**(1/2))+1):
        if n % i == 0:
            divisors.append((n//i, i)) # 약수쌍 저장
    return divisors

def solution(brown, yellow):  
    total = brown + yellow # 전체 격자의 수
    divisors = get_divisors(total)
    
    for w, h in divisors:
        if w < 3 or h < 3: # 가로, 세로 모두 3 이상이어야 가능
            continue
        if (w-2) * (h-2) == yellow:
            return [w, h]