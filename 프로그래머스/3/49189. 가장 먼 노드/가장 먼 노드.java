import java.util.*;

class Solution {
    public int solution(int n, int[][] edge) {
        int answer = 0;
        
        List<Integer>[] graph = new ArrayList[n+1]; // 노드 연결관계
        for (int i = 1; i <= n; i++) { // 배열 초기화; NullPointerException 방지
            graph[i] = new ArrayList<>();
        }
        for (int[] v: edge) {
            int a = v[0], b = v[1];
            graph[a].add(b);
            graph[b].add(a);
        }
        
        int[] dists = new int[n+1];
        Arrays.fill(dists, -1);
        dists[1] = 0;
        
        Queue<Integer[]> queue = new LinkedList<>();
        queue.offer(new Integer[]{1, 0}); // (노드 번호, 거리)
        
        while (!queue.isEmpty()) {
            Integer[] current = queue.poll();
            int curr = current[0], dist = current[1];
            
            for (Integer neighbor: graph[curr]) {
                if (dists[neighbor] == -1) {
                    dists[neighbor] = dist + 1;
                    queue.offer(new Integer[]{neighbor, dist+1});
                }
            } 
        }
        
        int maxDist = Arrays.stream(dists).max().getAsInt();
        
        for (int dist: dists) {
            if (dist == maxDist) {
                answer++;
            }
        }
        return answer;
    }
}