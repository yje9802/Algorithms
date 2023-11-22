class Solution {
    public int[][] solution(int n) {
        int[][] answer = new int[n][n];
        // answer에 채워질 숫자
        int num = 1;
        // 채워지는 행 시작/끝 인덱스, 채워지는 열 시작/끝 인덱스
        int rowS = 0;
        int rowE = n-1;
        int colS = 0;
        int colE = n-1;
        
        while (num <= n*n) {
            for (int i = colS; i <= colE; i++) {
                answer[rowS][i] = num;
                num++;
            }
            rowS++;
            
            for (int i = rowS; i <= rowE; i++) {
                answer[i][colE] = num;
                num++;
            }
            colE--;
            
            for (int i = colE; i >= colS; i--) {
                answer[rowE][i] = num;
                num++;
            }
            rowE--;
            
            for (int i = rowE; i >= rowS; i--) {
                answer[i][colS] = num;
                num++;
            }
            colS++;
        }
        return answer;
    }
}