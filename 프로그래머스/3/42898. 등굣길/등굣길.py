def solution(m, n, puddles):
    answer = 0
    
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1 # 시작위치
    
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            if [j+1, i+1] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007

    answer = dp[n-1][m-1]
    return answer