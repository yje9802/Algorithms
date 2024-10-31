def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries = deliveries[::-1] # 역순으로
    pickups = pickups[::-1]
    
    delivery, pick = 0, 0
    
    for i in range(n):
        delivery += deliveries[i]
        pick += pickups[i]
        
        while delivery > 0 or pick > 0:
            delivery -= cap
            pick -= cap
            answer += (n - i) * 2
        
        
    return answer