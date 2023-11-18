import java.math.BigInteger;

class Solution {
    public String solution(String a, String b) {
        String answer = "";
        BigInteger n_a = new BigInteger(a);
        BigInteger n_b = new BigInteger(b);
        BigInteger sum = n_a.add(n_b);
        answer = sum.toString();
        return answer;
    }
}