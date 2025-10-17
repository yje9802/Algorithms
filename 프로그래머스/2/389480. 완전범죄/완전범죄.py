def solution(info, n, m):
    INF = 10**9
    answer = INF
    
    things = len(info) # 훔쳐야 할 물건의 개수
    
    # dp[i][b]는 i번째 물건까지 훔쳤고, B의 누적 흔적 개수가 b일 때 A의 최소 흔적 개수
    dp = [[INF] * m for _ in range(things+1)]
    dp[0][0] = 0 # 아직 물건을 훔치지 않음
    
    for i in range(1, things+1):
        A_left, B_left = info[i-1] # 현재 물건 훔쳤을 때A와 B가 남기는 흔적 개수
        
        for b in range(m):
            if dp[i-1][b] == INF:
                continue
            # 이 물건을 A가 훔친다면
            new_A_left = dp[i-1][b] + A_left
            new_B_left = b
            if new_A_left < n:
                dp[i][new_B_left] = min(dp[i][new_B_left], new_A_left)
            
            # 이 물건을 B가 훔친다면
            new_A_left = dp[i-1][b]
            new_B_left = b + B_left
            if new_B_left < m:
                dp[i][new_B_left] = min(dp[i][new_B_left], new_A_left)
    
    for b in range(m):
        if dp[things][b] < INF:
            answer = min(answer, dp[things][b])
    
    if answer == INF: # 방법이 없음
        return -1
    return answer