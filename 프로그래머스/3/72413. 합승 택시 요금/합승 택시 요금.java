import java.util.*;

class Solution {
    
    static class Edge {
        int toNode;
        int cost;
        Edge(int toNode, int cost) {
            this.toNode = toNode;
            this.cost = cost;
        }
    }
    
    static final int INF = Integer.MAX_VALUE;
    
    public int solution(int n, int s, int a, int b, int[][] fares) {
        int answer = INF;
        
        List<List<Edge>> graph = new ArrayList<>();
        // graph 리스트 초기화
        for (int i = 0; i <= n; i++) graph.add(new ArrayList<>());
        for (int[] fare: fares) {
            int c = fare[0], d = fare[1], f = fare[2];
            graph.get(c).add(new Edge(d, f));
            graph.get(d).add(new Edge(c, f));
        }
        
        int[] distS = dijkstra(n, s, graph);
        int[] distA = dijkstra(n, a, graph); // 출발 지점이 A(A에서 역으로 노드i 까지의 비용이라 생각하면 됨)
        int[] distB = dijkstra(n, b, graph); // 출발 지점이 B
        
        for (int k = 1; k <= n; k++) {
            if (distS[k] == INF || distA[k] == INF || distB[k] == INF) continue;
            answer = Math.min(answer, distS[k] + distA[k] + distB[k]);
        }
            
        return answer;
    }
    
    static int[] dijkstra(int n, int src, List<List<Edge>> graph) {
        int[] dist = new int[n+1]; // dist[i]는 src에서 i 노드까지 가는 비용
        Arrays.fill(dist, INF); // 아직 계산되지 않은 노드는 INF로 초기화
        dist[src] = 0; // src -> src 비용은 0
        
        Queue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        pq.offer(new int[]{0, src});
        
        while (!pq.isEmpty()) {
            int[] temp = pq.poll();
            int currCost = temp[0], targetNode = temp[1];
            
            if (dist[targetNode] < currCost) continue; // 기존에 계산한 값이 더 작다면 그냥 넘어감
            
            for (Edge edge: graph.get(targetNode)) { // targetNode와 연결된 다른 노드들 확인
                int newCost = currCost + edge.cost;
                int nextNode = edge.toNode;
                // src에서 nextNode로 바로 갈 때보다 targetNode를 거쳐서 nextNode로 가는게 비용이 더 적게 들면 업데이트
                if (newCost < dist[nextNode]) {
                    dist[nextNode] = newCost;
                    pq.offer(new int[]{newCost, nextNode});
                }
            }
        }
        
        return dist;
    }
}