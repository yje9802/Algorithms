class Solution {
    int answer;
    int n;
    int[] hintCount;
    
    public int solution(int[][] cost, int[][] hint) {
        answer = Integer.MAX_VALUE;
        n = cost.length;
        hintCount = new int[n];
        
        dfs(0, 0, cost, hint);
        
        return answer;
    }
    
    private void dfs(int idx, int bundleCost, int[][] cost, int[][] hint) {
        if (idx == n - 1) {
            int totalCost = bundleCost;
            
            for (int stage = 0; stage < n; stage++) {
                int cnt = hintCount[stage];
                cnt = Math.min(cnt, cost[stage].length - 1);
                totalCost += cost[stage][cnt];
            }
            
            answer = Math.min(answer, totalCost);
            return;
        }
        
        // 번들을 사지 않음
        dfs(idx + 1, bundleCost, cost, hint);
        
        // idx번째 번들을 삼
        int price = hint[idx][0];
        for (int i = 1; i < hint[idx].length; i++) {
            int stage = hint[idx][i] - 1;
            hintCount[stage]++; // 해당 스테이지 힌트권 사용 수 up
        }
        dfs(idx + 1, bundleCost + price, cost, hint);
        
        // 백트래킹
        for (int i = 1; i < hint[idx].length; i++) {
            int stage = hint[idx][i] - 1;
            hintCount[stage]--;
        }
    }
}