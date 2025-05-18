import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int answer = -1;
        
        int n = maps.length, m = maps[0].length;
        boolean[][] visited = new boolean[n][m];
        visited[0][0] = true;
        
        Queue<Integer[]> queue = new LinkedList<>();
        queue.add(new Integer[]{0, 0, 1});
        
        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        
        while (!queue.isEmpty()) {
            Integer[] curr = queue.poll();
            int x = curr[0], y = curr[1], dist = curr[2];
            
            if (x == n-1 && y == m-1) {
                return dist;
            }
            
            for (int[] direction: directions) {
                int nx = x + direction[0], ny = y + direction[1];
                if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                    if (maps[nx][ny] == 1 && !visited[nx][ny]) {
                        visited[nx][ny] = true;
                        queue.add(new Integer[]{nx, ny, dist+1});
                    }
                }
            }
        }
        
        return answer;
    }
}