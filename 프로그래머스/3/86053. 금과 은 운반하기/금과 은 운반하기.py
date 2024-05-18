def solution(a, b, g, s, w, t):
    start = 0
    end = (10**9)*(10**5)*4 # 최악의 경우
    answer = end
    
    # 시간을 기준으로 이분 탐색
    while start <= end:
        mid = (start + end) // 2
        
        g_sum, s_sum, total = 0, 0, 0 # 지금까지 옮긴 금, 은, 금+은 
        
        for gold, silver, weight, time in zip(g, s, w, t):
            cnt = mid // (time * 2) # 주어진 시간 내에서 이동할 수 있는 총 횟수
            if mid % (time * 2) >= time: # 시간이 남으면 편도로 한 번 더 
                cnt += 1
            
            possible = cnt * weight # 주어진 시간 동안 운반할 수 있는 총량
            # weight는 횟수 한 번에 옮길 수 있는 양
            
            g_sum += gold if gold < possible else possible
            s_sum += silver if silver < possible else possible
            
            # 금 + 은 옮긴 총량은 possible을 넘어설 수 없음
            total += gold + silver if gold+silver < possible else possible
            
        if total >= a + b and g_sum >= a and s_sum >= b:
            end = mid - 1
            answer = min(answer, mid)
        else:
            start = mid + 1
        
    return answer

