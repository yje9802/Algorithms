import java.util.*;

class Solution {
    public int solution(int[][] routes) {
        int answer = 0;
        
        Arrays.sort(routes, (a, b) -> Integer.compare(a[1], b[1])); // 진출 시점이 빠른 순으로 정렬
        
        int camera = -30001; // 가장 최근 카메라 설치한 위치
        for (int[] route: routes) {
            if (route[0] > camera) {
                camera = route[1];
                answer++;
            }
        }
        
        return answer;
    }
}