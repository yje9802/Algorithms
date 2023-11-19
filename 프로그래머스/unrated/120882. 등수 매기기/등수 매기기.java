import java.util.*;

class Solution {
    public int[] solution(int[][] score) {
        int[] answer = new int[score.length];
        // 평균을 저장하는 리스트 
        // 어차피 모든 값을 똑같이 2로 나눠주기 때문에 그냥 영어,수학 점수의 합만 저장해도 된다.
        List<Integer> avgs = new ArrayList<>();
        for (int i = 0; i < score.length; i++) {
            avgs.add(score[i][0] + score[i][1]);
        }
        avgs.sort(Comparator.reverseOrder());
        
        for(int i = 0; i < score.length; i++){
            answer[i] = avgs.indexOf(score[i][0] + score[i][1])+1;
        }
        
        return answer;
    }
}