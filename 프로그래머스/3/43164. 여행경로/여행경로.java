import java.util.*;

class Solution {
    static String[][] tickets;
    static boolean[] used;
    static List<String> paths;
    
    public String[] solution(String[][] tickets) {
        String[] answer = {};
        
        this.tickets = tickets;
        // tickets 정렬(출발지(a) 기준 사전순 정렬, 출발지가 같다면 도착지(b) 기준 정렬)
        Arrays.sort(tickets, (a, b) -> {
            if (a[0].equals(b[0])) {
                return a[1].compareTo(b[1]);
            } else {
                return a[0].compareTo(b[0]);
            }
        });
        
        used = new boolean[tickets.length]; // 티켓 사용 여부
        paths = new ArrayList<>(); // 완성된 경로 모음
        
        dfs("ICN", "ICN", 1);
        answer = paths.get(0).split(" ");
        
        return answer;
    }
    
    void dfs(String curr, String path, int ticketCnt) {
        // curr: 현재 공항, path: 지금까지의 경로, ticketCnt: 티켓 사용 횟수
        if (ticketCnt == tickets.length + 1) {
            paths.add(path);
            return;
        }
        
        for (int i = 0; i < tickets.length; i++) {
            // 아직 사용한 적 없는 티켓이고, 현재 공항에서 출발하는 티켓인 경우
            if (!used[i] && tickets[i][0].equals(curr)) {
                used[i] = true;
                dfs(tickets[i][1], path + " " + tickets[i][1], ticketCnt + 1);
                used[i] = false; // 백트래킹
            }
        }
    }
}