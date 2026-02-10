def solution(n):
    answer = 0
    
    dp = [0] * n # 0번째 칸까지 채울 수 있는 경우의 수
    dp[0], dp[1] = 1, 2
    
    for i in range(2, n):
        dp[i] = (dp[i-2] + dp[i-1]) % 1000000007
    answer = dp[n-1]
    return answer