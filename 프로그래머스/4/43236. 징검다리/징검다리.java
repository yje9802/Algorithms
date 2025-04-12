import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int solution(int distance, int[] rocks, int n) {
        int answer = 0;
        
        Arrays.sort(rocks); // 이분탐색을 위한 정렬
        List<Integer> rocksL = Arrays.stream(rocks)
            .boxed()
            .collect(Collectors.toList());
        rocksL.add(distance);
        
        int left = 0, right = distance;
        
        while (left <= right) {
            int mid = (left + right) / 2;
            int removed = 0;
            int leftRock = 0;
            
            for (Integer rock: rocksL) {
                int dist = rock - leftRock;
                if (dist < mid) {
                    removed += 1;
                    if (removed > n) {
                        break;
                    }
                } else {
                    leftRock = rock;
                }
            }
            
            if (removed > n) {
                right = mid - 1;
            } else {
                answer = mid;
                left = mid + 1;
            }
        }
        
        return answer;
    }
}