import java.util.*;

class Solution {
    public int solution(int n, int[][] results) {
        int answer = 0;
        
        // key가 이긴 선수 리스트
        List<List<Integer>> winGraph = new ArrayList<>();
        // key를 이긴 선수 리스트
        List<List<Integer>> loseGraph = new ArrayList<>();
        
        // graphs 초기화
        for (int i = 0; i < n+1; i++) {
            winGraph.add(new ArrayList<>());
            loseGraph.add(new ArrayList<>());
        }
        
        for (int[] result: results) {
            int win = result[0], lose = result[1];
            winGraph.get(win).add(lose);
            loseGraph.get(lose).add(win);
        }
        
        for (int p = 1; p < n+1; p++) {
            Set<Integer> winVisited = new HashSet<>();
            Set<Integer> loseVisited = new HashSet<>();
            
            int winCount = dfs(p, winGraph, winVisited);
            int loseCount = dfs(p, loseGraph, loseVisited);
            
            // 승패를 모두 가려냄
            if (winCount + loseCount == n-1) {
                answer++;
            }
        }
        
        return answer;
    }
    
    static int dfs(int start, List<List<Integer>> graph, Set<Integer> visited) {
        int count = 0; // 이긴/진 선수 수
        for (Integer player: graph.get(start)) {
            if (!visited.contains(player)) {
                visited.add(player);
                count += 1 + dfs(player, graph, visited);
            }
        }
        return count;
    }
}