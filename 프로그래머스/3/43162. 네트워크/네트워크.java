class Solution {
    static boolean[] visited;
    
    public int solution(int n, int[][] computers) {
        int answer = 0;
        visited = new boolean[n];
        
        for (int v = 0; v < n; v++) {
            if (!visited[v]) {
                dfs(v, n, computers);
                answer++;
            }
        }
        
        return answer;
    }
    
    void dfs(int v, int n, int[][] computers) {
        visited[v] = true;
        
        for (int nodeN = 0; nodeN < n; nodeN++) {
            if (!visited[nodeN] && computers[v][nodeN] == 1) {
                dfs(nodeN, n, computers);
            }
        }
    }
}