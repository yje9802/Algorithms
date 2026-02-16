class Solution {
    static final long MOD = 1_000_000_007;
    
    public long solution(int n) {
        long answer = 0;
        
        if (n % 2 == 1) return answer;
        
        long[] dp = new long[n+1];
        dp[2] = 3; // 최소 단위

        for (int i = 4; i < n+1; i+=2) {
            dp[i] = dp[i-2] * 3 + 2;
            
            for (int j = i - 4; j > 0; j-=2) {
                dp[i] += dp[j] * 2;
            }
            dp[i] = dp[i] % MOD;
        }
        
        answer = dp[n];
        return answer;
    }
}