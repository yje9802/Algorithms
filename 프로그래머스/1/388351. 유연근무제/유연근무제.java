import java.util.*;

class Solution {
    public int solution(int[] schedules, int[][] timelogs, int startday) {
        int answer = 0;
        
        for (int i = 0; i < schedules.length; i++) {
            int schedule = schedules[i];
            int limit = calcLimit(schedule); // 출근 희망 시각 + 10분 계산
            
            int today = startday;
            int cnt = 0;
            for (int log: timelogs[i]) {
                if (today >= 6) { // 주말이라면
                    today = today % 7 + 1;
                    continue;
                }
                if (log <= limit) {
                    cnt++;
                } else {
                    break;
                }
                today++;
            }
            if (cnt == 5) {
                answer++;
            }
        }
        
        return answer;
    }
    
    private int calcLimit(int schedule) {
        int plused = schedule % 100 + 10;
        int newHour = schedule / 100 + (plused / 60);
        int newMinute = plused % 60;
        return newHour * 100 + newMinute;
    }
}