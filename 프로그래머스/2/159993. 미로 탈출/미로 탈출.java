import java.util.*;

class Solution {
    int n, m;
    int[][] directions = { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
    
    public int solution(String[] maps) {
        int answer = 0;
        
        n = maps.length;
        m = maps[0].length();
        
        int[] S = null, L = null, E = null;
        
        outer:
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                char cell = maps[i].charAt(j);
                if (cell == 'S') S = new int[]{i, j};
                else if (cell == 'L') L = new int[]{i, j};
                else if (cell == 'E') E = new int[]{i, j};
                
                if (S != null && L != null && E != null) {
                    break outer;
                }
            }
        }
        
        int toLever = bfs(S, L, maps);
        int toEnd = bfs(L, E, maps);
        
        if (toLever == -1 || toEnd == -1) {
            answer = -1;
        } else {
            answer = toLever + toEnd;
        }
        
        return answer;
    }
    
    int bfs(int[] start, int[] end, String[] maps) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{ start[0], start[1], 0 });
        
        boolean[][] visited = new boolean[n][m];
        visited[start[0]][start[1]] = true;
        
        while (!queue.isEmpty()) {
            int[] temp = queue.poll();
            int x = temp[0], y = temp[1], cost = temp[2];
            
            if (x == end[0] && y == end[1]) return cost;
            
            for (int[] dir: directions) {
                int nx = x + dir[0], ny = y + dir[1];
                
                if (nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[nx][ny]) {
                    char curr = maps[nx].charAt(ny);
                    if (curr == 'X') continue;
                    visited[nx][ny] = true;
                    queue.offer(new int[]{ nx, ny, cost + 1 });
                }
            }
        }
        
        return -1;
    }
}