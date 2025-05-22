import java.util.*;

class Solution {
    static boolean[] visited;
    
    public int solution(int n, int[][] computers) {
        int answer = 0;
        visited = new boolean[n];
        
        for (int v = 0; v < n; v++) {
            if (!visited[v]) {
                bfs(v, computers);
                answer++;
            }
        }
        
        return answer;
    }
    
    void bfs(int start, int[][] computers) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);
        visited[start] = true;
        
        while(!queue.isEmpty()) {
            int curr = queue.poll();
            
            for (int i = 0; i < computers.length; i++) {
                if (computers[curr][i] == 1 && !visited[i]) {
                    queue.add(i);
                    visited[i] = true;
                }
            }
        }
    }
}