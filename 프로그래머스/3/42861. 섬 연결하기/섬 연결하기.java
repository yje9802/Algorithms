import java.util.*;

class Solution {
    static int[] parents;
    
    public int solution(int n, int[][] costs) {
        int answer = 0;
        
        // 간선 가중치 오름차순 정렬
        Arrays.sort(costs, (a, b) -> Integer.compare(a[2], b[2]));
        
        // union-find용
        parents = new int[n];
        for (int i = 0; i < n; i++) parents[i] = i;
        
        int edgeCount = 0; // 선택한 간선 수
        
        for (int[] edge: costs) {
            int a = edge[0], b = edge[1], cost = edge[2];
            
            if (union(a, b)) { // 둘이 합쳐진다면 선택 가능
                answer += cost;
                edgeCount++;
                
                if (edgeCount == n-1) break; // 선택한 간선의 수가 n-1 개가 되면 종료
            }
        }
        
        return answer;
    }
    
    static int find(int x) {
        if (parents[x] != x) {
            parents[x] = find(parents[x]);
        }
        return parents[x];
    }
    
    static boolean union(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        
        if (rootX != rootY) {
            parents[rootY] = rootX;
            return true;
        }
        return false;
    }
}