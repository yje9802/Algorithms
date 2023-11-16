class Solution {
    public int solution(int[][] board) {
        int answer = 0;
        
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                // 지뢰 발견
                if (board[i][j] == 1) {
                    for (int y = -1; y < 2; y++) {
                        int p = i + y;
                        // 지뢰가 맨 윗줄이나 맨 아래줄에 있는 경우
                        if (p < 0 || p == board.length) {
                            continue;
                        } else {
                            for (int x = -1; x < 2; x++) {
                                int q = j + x;
                                if (q < 0 || q == board[0].length) {
                                    continue;
                                } else {
                                    if (board[p][q] == 0) {
                                        board[p][q] = 2;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j] == 0) {
                    answer += 1;
                }
            }
        }
        return answer;
    }
}