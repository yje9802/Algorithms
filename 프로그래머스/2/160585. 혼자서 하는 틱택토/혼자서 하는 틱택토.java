class Solution {
    public int solution(String[] board) {
        int answer = 0;
        
        int[] count = new int[2]; // 0번 인덱스가 선공의 개수
        
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[i].charAt(j) == 'O') count[0] += 1;
                else if (board[i].charAt(j) == 'X') count[1] += 1;
            }
        }
        
        if (count[0] == 0 && count[1] == 0) return 1; // 아직 시작 전
        if (count[0] < count[1]) return 0; // 'X'의 개수가 더 많을 수 없음
        
        if (count[0] - count[1] > 1) return 0;

        boolean OWin = checkWinner(board, 'O'), XWin = checkWinner(board, 'X');
        if (OWin && !XWin && count[0] > count[1]) return 1;
        if (!OWin && XWin && count[0] == count[1]) return 1;
        if (OWin == false && XWin == false) return 1;
        
        return answer;
    }
    
    // 승자가 존재하는지 체크
    private boolean checkWinner(String[] board, char p) {
        // 가로
        for (int i = 0; i < 3; i++) {
            if (board[i].charAt(0) == p && board[i].charAt(1) == p && board[i].charAt(2) == p) return true;
        }
        // 세로
        for (int j = 0; j < 3; j++) {
            if (board[0].charAt(j) == p && board[1].charAt(j) == p && board[2].charAt(j) == p) return true;
        }
        // 대각선
        if (board[0].charAt(0) == p && board[1].charAt(1) == p && board[2].charAt(2) == p) return true;
        if (board[0].charAt(2) == p && board[1].charAt(1) == p && board[2].charAt(0) == p) return true;

        return false;
    }
}