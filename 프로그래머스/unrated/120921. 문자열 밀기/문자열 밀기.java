class Solution {
    public int solution(String A, String B) {
        int answer = -1;
        int cnt = 0;
        if (B.equals(A)) {
            answer = 0;
            return answer;
        }
        for (int i = 0; i < A.length(); i++) {
            A = A.charAt(A.length()-1) + A.substring(0, A.length()-1);
            cnt++;
            if (B.equals(A)) {
                answer = cnt;
                return answer;
            }
        }

        return answer;
    }
}