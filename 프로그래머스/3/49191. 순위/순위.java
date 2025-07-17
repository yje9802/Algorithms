import java.util.*;

class Solution {
    public int solution(int n, int[][] results) {
        int answer = 0;
        
        // 각 선수 간의 알려진 승패 기록
        int[][] graph = new int[n+1][n+1]; // 0은 승패모름, 1은 이김, 0은 짐
        for (int[] result: results) {
            int win = result[0], lose = result[1];
            graph[win][lose] = 1;
            graph[lose][win] = -1;
        }
        
        for (int i = 1; i < n+1; i++) {
            for (int j = 1; j < n+1; j++) {
                if (graph[i][j] == 1) {
                    for (int k = 1; k < n+1; k++) {
                        if (graph[j][k] == 1) {
                            graph[i][k] = 1;
                            graph[k][i] = -1;
                        } else if (graph[i][k] == -1) {
                            graph[j][k] = -1;
                            graph[k][j] = 1;
                        }
                    }
                }
            }
        }
        
        for (int i = 1; i < n+1; i++) {
            int count = 0;
            for (int g: graph[i]) {
                if (g != 0) {
                    count++;
                }
            }
            if (count == n-1) {
                answer++;
            }
        }
        
        return answer;
    }
}