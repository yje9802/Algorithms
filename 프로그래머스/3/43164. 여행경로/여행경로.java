import java.util.*;

class Solution {
    static List<String> paths;
    static boolean[] used;
    static String[][] tickets;
    
    public String[] solution(String[][] tickets) {
        this.tickets = tickets;
        Arrays.sort(tickets, (a, b) -> {
            if (a[0].equals(b[0])) {
                return a[1].compareTo(b[1]); // 출발지가 같으면 도착지 기준 정렬
            } else {
                return a[0].compareTo(b[0]); // 출발지 기준 정렬
            }
        });
        
        used = new boolean[tickets.length];
        paths = new ArrayList<>();
        
        dfs("ICN", "ICN", 1);
        
        return paths.get(0).split(" ");
    }
    
    void dfs(String curr, String path, int depth) {
        // curr는 현재 공항, path는 현재까지의 경로, depth는 티켓 사용 횟수
        if (depth == tickets.length + 1) { // 티켓 모두 사용 완료
            paths.add(path);
            return;
        }
        
        for (int i = 0; i < tickets.length; i++) {
            if (!used[i] && tickets[i][0].equals(curr)) {
                used[i] = true;
                dfs(tickets[i][1], path + " " + tickets[i][1], depth + 1);
                used[i] = false;
            }
        }
    }
}