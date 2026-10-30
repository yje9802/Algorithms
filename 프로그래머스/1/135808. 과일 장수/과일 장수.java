import java.util.*;

class Solution {
    public int solution(int k, int m, int[] score) {
        int answer = 0;
        
        // score 내림차순 정렬
        Arrays.sort(score);
        for (int i = 0; i < score.length / 2; i++) {
            int temp = score[i];
            score[i] = score[score.length - 1 - i];
            score[score.length - 1 - i] = temp;
        }
        
        for (int i = 0; i < score.length; i = i + m) {
            int[] apples = Arrays.copyOfRange(score, i, i+m);
            answer += Arrays.stream(apples).min().getAsInt() * m; // 사실 apples의 마지막 원소가 최솟값
        }
        return answer;
    }
}