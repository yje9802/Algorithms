def solution(n):
    answer = 0
    MOD = 1000000007
    
    if n % 2 == 1: # 가로의 길이가 홀수인 경우 제외
        return answer
    
    dp = [0] * (n+1)
    dp[0] = 1
    dp[2] = 3 # 가로의 길이가 2일 때 채울 수 있는 경우의 수

    for i in range(4, n+1, 2):
        dp[i] = dp[i-2] * 3 + 2 # + 2는 가로의 길이가 i일 때 채울 수 있는 방법의 수는 항상 2이기 때문
        
        for j in range(i-4, 0, -2):
            dp[i] += dp[j] * 2
        dp[i] = dp[i] % MOD
        
    answer = dp[n]
    return answer