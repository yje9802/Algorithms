import java.util.*;

class Solution {
    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        int answer = 0;
        
        int MAX = 102;
        int[][] board = new int[MAX][MAX];
        
        // 사각형 영역 1로 채우기
        for (int[] rec: rectangle) {
            int x1 = rec[0]*2, y1 = rec[1]*2, x2 = rec[2]*2, y2 = rec[3]*2;
            for (int i = x1; i < x2+1; i++) {
                for (int j = y1; j < y2+1; j++) {
                    board[i][j] = 1;
                }
            }
        }
        
        // 테두리만 1로 남기고, 내부는 0으로
        for (int[] rec: rectangle) {
            int x1 = rec[0]*2, y1 = rec[1]*2, x2 = rec[2]*2, y2 = rec[3]*2;
            for (int i = x1+1; i < x2; i++) {
                for (int j = y1+1; j < y2; j++) {
                    board[i][j] = 0;
                }
            }
        }
        
        // BFS 시작
        int[][] visited = new int[MAX][MAX];
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{characterX*2, characterY*2}); // 캐릭터 시작 위치
        visited[characterX*2][characterY*2] = 1;
        
        int[] dx = new int[]{-1, 1, 0, 0};
        int[] dy = new int[]{0, 0, -1, 1};
        
        while (!queue.isEmpty()) {
            int[] loc = queue.poll();
            int x = loc[0], y = loc[1];
            
            if (x == itemX*2 && y == itemY*2) { // 목적지 도달
                return (visited[x][y]-1) / 2;
            }
            
            for (int n = 0; n < 4; n++) {
                int nx = x + dx[n], ny = y + dy[n];
                if (board[nx][ny] == 1 && visited[nx][ny] == 0) { // 아직 간 적 없는 테두리
                    visited[nx][ny] = visited[x][y] + 1;
                    queue.add(new int[]{nx, ny});
                }
            }
        }
        
        return answer;
    }
}