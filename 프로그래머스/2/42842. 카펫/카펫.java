import java.util.*;

class Solution {
    static List<int[]> divisors = new ArrayList<>();
    
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        
        int total = brown + yellow;
        getDivisors(total);
        
        for (int[] divisor: divisors) {
            int w = divisor[0], h = divisor[1];
            if (w < 3 || h < 3) {
                continue;
            } else {
                if ((w-2) * (h-2) == yellow) {
                    answer[0] = w;
                    answer[1] = h;
                }
            }
        }
        return answer;
    }
    
    private void getDivisors(int n) {
        for (int i = 1; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                divisors.add(new int[]{n / i, i});
            }
        }
    }
}