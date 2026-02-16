class Solution {
    static final long MOD = 1_000_000_007;
    
    public long solution(int n) {
        long answer = 0;
        
        if (n % 2 == 1) return answer;
        
        long[] dp = new long[n+1];
        dp[2] = 3; // 최소 단위

        long extra = 0;
        
        for (int i = 4; i < n+1; i+=2) {
            extra += dp[i-4];
            dp[i] = dp[i-2] * 3 + extra * 2 + 2;
            dp[i] = dp[i] % MOD;
        }
        
        answer = dp[n];
        return answer;
    }
}