class Solution {
    public int solution(int a, int b) {
        int lastB = b / gcd(a, b);
        
        while (lastB != 1) {
            if (lastB % 2 == 0) {
                lastB /= 2;
            } else if (lastB % 5 == 0) {
                lastB /= 5;
            } else {
                // 2나 5로 나누어 떨어지지 않는다면
                return 2;
            }
        }
        
        return 1;
    }
    
    private int gcd(int a, int b) {
        if (b == 0) {
            return a;
        } else {
            return gcd(b, a % b);
        }
    }
}