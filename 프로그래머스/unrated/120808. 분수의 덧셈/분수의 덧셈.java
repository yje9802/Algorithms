class Solution {
    public int GCD(int num1, int num2) {
        if (num1 % num2 == 0) {
            return num2;
        }
        return GCD(num2, num1 % num2);
    }
    
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        if (numer1 > 0 && numer1 < 1000 && numer2 > 0 && numer2 < 1000 && denom1 > 0 && denom1 < 1000 && denom2 > 0 && denom2 < 1000) {
            numer1 = numer1 * denom2;
            numer2 = numer2 * denom1;
        }
        int[] answer = new int[]{numer1 + numer2, denom1 * denom2};
            
            int gcd = GCD(answer[0], answer[1]);
            answer[0] /= gcd;
            answer[1] /= gcd;
        return answer;
    }
}