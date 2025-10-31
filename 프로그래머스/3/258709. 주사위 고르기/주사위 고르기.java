import java.util.*;

class Solution {
    static List<List<Integer>> combs = new ArrayList<>();
    
    public int[] solution(int[][] dice) {
        int[] answer;
        
        int n = dice.length; // 주사위의 개수
        int maxWin = -1;
        List<Integer> bestComb = new ArrayList<>();
        
        boolean[] visited = new boolean[n];
        combinations(dice, visited, 0, n, n/2);
        
        for (List<Integer> comb: combs) {
            List<int[]> A = new ArrayList<>();
            for (Integer a: comb) A.add(dice[a]);
            
            List<int[]> B = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                if (!comb.contains(i)) B.add(dice[i]);
            }
            
            int[] ASums = getSums(A);
            int[] BSums = getSums(B);
            
            int winCases = 0;
            for (int a: ASums) {
                winCases += findLowerCnt(BSums, a);
            }
            
            if (winCases > maxWin) {
                maxWin = winCases;
                bestComb = comb;
            }
        }
        answer = bestComb.stream().mapToInt(i->i+1).toArray();
        return answer;
    }
    
    public static void combinations(int[][] arr, boolean[] visited, int start, int n, int r) {
        if (r == 0) {
            List<Integer> comb = new ArrayList<>();
            for (int i = 0; i < n; i++) {
                if (visited[i]) comb.add(i);
            }
            combs.add(comb);
            return;
        }
        
        for (int i = start; i < n; i++) {
            visited[i] = true;
            combinations(arr, visited, i+1, n, r-1);
            visited[i] = false;
        }
    }
    
    public static int[] getSums(List<int[]> dices) {
        List<Integer> sums = new ArrayList<>();
        dfs(dices, 0, 0, sums);
        Collections.sort(sums);
        return sums.stream().mapToInt(i->i).toArray();
    }
    
    public static void dfs(List<int[]> dices, int idx, int currSum, List<Integer> sums) {
        if (idx == dices.size()) {
            sums.add(currSum);
            return;
        }
        for (int face: dices.get(idx)) {
            dfs(dices, idx+1, currSum + face, sums);
        }
    }
    
    public static int findLowerCnt(int[] arr, int target) {
        int left = 0, right = arr.length;
        
        while (left < right) {
            int mid = (left + right) / 2;
            if (arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
}