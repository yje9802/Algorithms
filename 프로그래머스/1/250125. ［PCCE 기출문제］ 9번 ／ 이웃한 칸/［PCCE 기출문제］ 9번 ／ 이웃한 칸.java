class Solution {
    public int solution(String[][] board, int h, int w) {
        int answer = 0;
        int n = board.length; // 보드판 크기
        
        int[][] directions = new int[][]{ {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
        
        String color = board[h][w];
        
        for (int[] dir: directions) {
            int nh = h + dir[0], nw = w + dir[1];
            if (nh >= 0 && nh < n && nw >= 0 && nw < n) {
                if (board[nh][nw].equals(color)) answer++;
            }
        }
        
        return answer;
    }
}