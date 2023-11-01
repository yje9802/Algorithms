class Solution {
    public int solution(int num, int k) {
        int answer = -1;
        String s_num = "" + num;
        answer = s_num.indexOf(String.valueOf(k));
        
        answer = answer >= 0 ? answer + 1 : -1;
        return answer;
    }
}