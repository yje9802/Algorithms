import java.util.*;

class Solution {
    public int solution(String[][] book_time) {
        int answer = 0;
        
        Queue<int[]> times = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        for (String[] time: book_time) {
            int[] minutes = new int[] {convertTime(time[0]), convertTime(time[1]) + 10};
            times.add(minutes);
        }
        
        Queue<Integer> rooms = new PriorityQueue<>();
        rooms.offer(times.poll()[1]);
        answer++;
        while (!times.isEmpty()) {
            int[] curr = times.poll();
            Integer earlist = rooms.poll();
            rooms.offer(curr[1]);
            
            if (earlist > curr[0]) {
                rooms.offer(earlist);
                answer++;
            }
        }
        
        return answer;
    }
    
    int convertTime(String stringTime) {
        String[] time = stringTime.split(":");
        int hour = (Integer.parseInt(time[0])) * 60;
        int minute = Integer.parseInt(time[1]);
        return hour + minute;
    }
}