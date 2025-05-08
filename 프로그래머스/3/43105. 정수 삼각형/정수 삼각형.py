def solution(triangle):
    answer = 0
    
    dp = [[] for _ in range(len(triangle))] # 해당 칸의 최대값 저장 dp 테이블
    
    dp[0].append(triangle[0][0])
    
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i].append(dp[i-1][0] + triangle[i][j])
            elif j == len(triangle[i]) - 1:
                dp[i].append(dp[i-1][-1] + triangle[i][j])
            else:
                dp[i].append(max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j])
    
    answer = max(dp[-1])
    return answer