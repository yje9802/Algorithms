class Solution {
    public int solution(int n, int w, int num) {
        int answer = 1;
        
        int quotient = num / w;
        int mod = num % w;
        int[] xy = findRowAndColumn(quotient, mod, w);
        int x = xy[0], y = xy[1]; // 꺼내려는 상자가 위치한 행과 열
        
        int[] lastXY = findRowAndColumn(n / w, n % w, w);
        int lastX = lastXY[0], lastY = lastXY[1]; // 마지막 상자가 위치한 행과 열
        
        if (lastX % 2 == 0) {
            if (lastY < y) {
                answer += lastX - x - 1;
            } else {
                answer += lastX - x;
            }
        } else {
            if (lastY <= y) {
                answer += lastX - x;
            } else {
                answer += lastX - x - 1;
            }
        }
        
        return answer;
    }
    
    // 특정 상자가 위치한 행, 열 구하는 메서드
    static int[] findRowAndColumn(int quotient, int mod, int w) {
        int[] xy = new int[2];
        
        if (mod == 0) {
            xy[0] = quotient - 1;
            if (quotient % 2 != 0) xy[1] = w - 1;
        } else {
            xy[0] = quotient;
            if (quotient % 2 == 0) xy[1] = mod - 1;
            else xy[1] = w - mod;
        }
        
        return xy;
    }
}