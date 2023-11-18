class Solution {
    public int solution(int[][] lines) {
        int answer = 0;
        // 선분의 양 끝점이 -100에서 100까지 가능하기 때문
        // 0은 -100, 100은 0, 200은 100을 의미한다.
        int[] drawLine = new int[200]; 
        for (int i = 0; i < 3; i++) {
            // lines에 선분을 표시
            for (int j = lines[i][0] + 100; j < lines[i][1] + 100; j++) {
                drawLine[j]++;
            }
        }
        
        for (int i = 0; i < 200; i++) {
            if (drawLine[i] > 1) {
                answer++;
            }
        }
        
        return answer;
    }
}