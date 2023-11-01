class Solution {
    public int solution(int n) {
        int answer = 0;
        String sn = ""+n;
        int n_len = sn.length();
        
        for (int i = 0; i < n_len; i++) {
            answer += n % 10;
            n /= 10;
        }
        return answer;
    }
}