import java.util.*;

class Solution {
    int r, c;
    
    public int solution(int[] mats, String[][] park) {
        int answer = -1;
        r = park.length;
        c = park[0].length;
        
        Integer[] boxedMats = Arrays.stream(mats).boxed().toArray(Integer[]::new);
        Arrays.sort(boxedMats, Collections.reverseOrder());
        
        for (Integer m: boxedMats) {
            for (int i = 0; i < r-m+1; i++) {
                for (int j = 0; j < c-m+1; j++) {
                    if (canPlace(i, j, m, park)) return m;
                }
            }
        }
        
        return answer;
    }
    
    private boolean canPlace(int row, int column, int size, String[][] park) {
        if (row + size > r || column + size > c) return false;
        for (int i = row; i < row+size; i++) {
            for (int j = column; j < column+size; j++) {
                if (!park[i][j].equals("-1")) return false;
            }
        }
        return true;
    }
}