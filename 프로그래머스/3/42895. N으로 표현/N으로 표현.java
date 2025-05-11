import java.util.*;

class Solution {
    public int solution(int N, int number) {
        int answer = -1;
        
        if (N == number) return 1;
        
        // dp[i]는 N을 i번 사용해서 만들 수 있는 수들의 집합
        List<Set<Integer>> dp = new ArrayList<>();
        dp.add(new HashSet<>()); // 0번 인덱스는 사용 X
        
        for (int i = 1; i < 9; i++) {
            Set<Integer> currentSet = new HashSet<>();
            
            // 숫자 이어붙여서 만들고 set에 저장
            int repeatedNum = Integer.parseInt(String.valueOf(N).repeat(i));
            currentSet.add(repeatedNum);
            
            for (int j = 1; j < i; j++) {
                for (Integer n1: dp.get(j)) {
                    for (Integer n2: dp.get(i-j)) {
                        currentSet.add(n1 + n2);
                        currentSet.add(n1 - n2);
                        currentSet.add(n1 * n2);
                        if (n2 != 0) {
                            currentSet.add(n1 / n2);
                        }
                    }
                }
            }
            
            // i번 사용해서 number를 만들 수 있는 경우
            if (currentSet.contains(number)) {
                return i;
            }
            
            dp.add(currentSet);
        }
        
        return answer;
    }
}