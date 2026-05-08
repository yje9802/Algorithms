def solution(cost, hint):
    answer = float('inf')
    
    n = len(cost) # 스테이지 개수
    hint_count = [0] * n
    
    def dfs(idx, total_bundle_cost):
        nonlocal answer
        
        if idx == n - 1: # 모든 힌트 번들 구매 여부 결정끝(dfs 종료 조건)
            total = total_bundle_cost
            
            for stage in range(n):
                cnt = min(hint_count[stage], len(cost[stage]) - 1)
                total += cost[stage][cnt]
            
            answer = min(answer, total)
            return
        
        # idx번 힌트 번들 구매 X
        dfs(idx + 1, total_bundle_cost)
        
        # idx번 힌트 번들 구매 O
        bundle = hint[idx]
        price = bundle[0] # 힌트 번들 구매 가격
        stages = bundle[1:] # 힌트권 번호들
        
        for stage in stages:
            hint_count[stage - 1] += 1
            
        dfs(idx+1, total_bundle_cost + price)
        
        # 원상복구
        for stage in stages:
            hint_count[stage - 1] -= 1
    
    dfs(0, 0)
    return answer