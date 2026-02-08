import java.util.*;

class Solution {
    public int solution(String[][] book_time) {
        int answer = 0;
        
        int MAX = 24 * 60 + 10;
        int[] rooms = new int[MAX+2];
        
        for (String[] booked: book_time) {
            int start = convertTime(booked[0]);
            int end = convertTime(booked[1]) + 10;
            rooms[start] += 1;
            rooms[end] -= 1;
        }
        
        for (int i = 1; i < rooms.length; i++) {
            rooms[i] = rooms[i-1] + rooms[i];
            answer = Math.max(answer, rooms[i]);
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