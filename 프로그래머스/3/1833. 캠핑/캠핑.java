import java.util.*;

class Solution {
    public int solution(int n, int[][] data) {
        int answer = 0;
        
        Arrays.sort(data, (a, b) -> Integer.compare(a[0], b[0]));
        
        for (int i = 0; i < n; i++) {
            int x1 = data[i][0], y1 = data[i][1];
            
            for (int j = i+1; j < n; j++) {
                int x2 = data[j][0], y2 = data[j][1];
                
                // 넓이가 0이면 넘어감
                if (x1 == x2 || y1 == y2) {
                    continue;
                }
                
                boolean isInside = false; // 쐐기가 내부에 포함되는지 여부
                for (int k = i+1; k < j; k++) {
                    int p1 = data[k][0], p2 = data[k][1];
                    if ((x1 < p1 && p1 < x2) && (Math.min(y1, y2) < p2 && p2 < Math.max(y1, y2))) {
                        isInside = true;
                        break;
                    }
                }
                if (!isInside) answer++;
            }
        }
        return answer;
    }
}