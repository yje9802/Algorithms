import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;
        
        Set<Integer> lostSet = new HashSet<>();
        Set<Integer> reserveSet = new HashSet<>();
        
        for (int r: reserve) {
            reserveSet.add(r);
        }
        
        // 여벌 체육복을 가져온 학생이 체육복을 도난당한 경우 제거
        for (int l: lost) {
            if (reserveSet.contains(l)) {
                reserveSet.remove(l);
            } else {
                lostSet.add(l);
            }
        }
        
        // lostSet을 순회하면서 동시에 요소를 삭제하게 되면 문제가 생기기 때문에
        // lostSet의 복사본으로 순회
        for (int i : new HashSet<>(lostSet)) {
            if (reserveSet.contains(i-1)) {
                lostSet.remove(i);
                reserveSet.remove(i-1);
            } else if (reserveSet.contains(i+1)) {
                lostSet.remove(i);
                reserveSet.remove(i+1);
            }
        }
        
        answer = n - lostSet.size();
        
        return answer;
    }
}