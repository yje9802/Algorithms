import java.util.*;

class Solution {
    static Set<Integer> nums = new HashSet<>();
    static boolean[] visited;
    
    public int solution(String numbers) {
        int answer = 0;
        visited = new boolean[numbers.length()];
        permutations("", numbers);
        
        for (int n: nums) {
            if (isPrime(n)) {
                answer++;
            }
        }
        return answer;
    }
    
    // 순열 조합 만드는 메서드
    void permutations(String current, String numbers) {
        if (!current.equals("")) { // 현재 만든 숫자(current) 저장
            nums.add(Integer.parseInt(current));
        }
        
        for (int i = 0; i < numbers.length(); i++) {
            if (!visited[i]) {
                visited[i] = true;
                permutations(current + numbers.charAt(i), numbers); // current에 다음 글자 추가
                visited[i] = false; // 백트래킹
            }
        }
    }
    
    boolean isPrime(int n) {
        if (n < 2) return false;
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0) return false;
        }
        return true;
    }
}