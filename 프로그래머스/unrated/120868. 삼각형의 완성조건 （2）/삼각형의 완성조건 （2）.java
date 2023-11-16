import java.util.Arrays;

class Solution {
    public int solution(int[] sides) {
        int answer = 0;
        Arrays.sort(sides);
        int min = sides[0];
        int max = sides[1];
        // max가 가장 긴 변일 경우
        for (int i = max - min + 1; i <= max; i++) {
            answer++;
        }
        // 나머지 한 변이 가장 긴 변일 경우
        // 가장 짧은 변보다는 길어야 하고 min+max 보다는 작아야 함
        for (int i = max + 1; i < min + max; i++) {
            answer++;
        }
        return answer;
    }
}