def solution(n, times):
    answer = 0
    
    left = min(times)
    # 심사가 가장 오래 걸리는 심사대에서 모두가 심사 받는 경우
    right = max(times) * n
    
    while left <= right:
        mid = (left + right) // 2
        checked = 0
        
        for time in times:
            checked += mid // time
            if checked >= n:
                break
                
        # 심사한 사람의 수가 심사 받아야할 사람의 수(n)보다 많거나 같은 경우 -> 일단 현재 mid 시간으로 충분 -> 더 최소인 시간이 있을 수 있음
        if checked >= n:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer