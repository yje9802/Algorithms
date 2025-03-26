import java.util.*;

class Solution {
    public int[] solution(int[][] edges) {
        int[] answer = new int[4];
        
        // 정점 번호 : [나가는 간선 수, 들어오는 간선 수]
        Map<Integer, int[]> nodes = new HashMap<>();
        
        for (int[] edge : edges) {
            int a = edge[0], b = edge[1];
            
            // 초기값 설정
            nodes.putIfAbsent(a, new int[]{0, 0});
            nodes.putIfAbsent(b, new int[]{0, 0});
            
            nodes.get(a)[0]++; // a에서 나가는 간선 증가
            nodes.get(b)[1]++; // b로 들어오는 간선 증가
        }
        
        for (Map.Entry<Integer, int[]> entry: nodes.entrySet()) {
            int key = entry.getKey();
            int outCount = entry.getValue()[0];
            int inCount = entry.getValue()[1];
            
            if (outCount >= 2 && inCount == 0) {
                answer[0] = key;
            } else if (outCount == 0 && inCount > 0) { // 막대그래프
                answer[2]++;
            } else if (outCount >= 2 && inCount >= 2) {
                answer[3]++;
            }
        }
        
        answer[1] = nodes.get(answer[0])[0] - answer[2] - answer[3]; // 도넛 그래프 개수 계산
            
        return answer;
    }
}