class Solution {
    static final int MOD = 10007;
    
    public int solution(int n, int[] tops) {
        int answer = 0;
        
        int[] notRight = new int[n];
        int[] right = new int[n];
        
        notRight[0] = tops[0] == 1 ? 3 : 2;
        right[0] = 1;
        
        for (int i = 1; i < n; i++) {
            int nr = notRight[i-1];
            int r = right[i-1];
            
            if (tops[i] == 1) {
                notRight[i] = (3 * nr + 2 * r) % MOD;
            } else {
                notRight[i] = (2 * nr + 1 * r) % MOD;
            }
            right[i] = (1 * nr + 1 * r) % MOD;
        }
        
        answer = (notRight[n-1] + right[n-1]) % MOD;
        return answer;
    }
}