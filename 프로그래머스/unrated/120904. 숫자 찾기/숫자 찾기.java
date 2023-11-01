class Solution {
    public int solution(int num, int k) {
        int answer = -1;
        String s_num = "" + num;
        String[] ss_num = s_num.split("");
        
        for (int i = 0; i < ss_num.length; i++) {
            if (Integer.parseInt(ss_num[i]) == k) {
                answer = i + 1;
                break;
            }
        }
        
        return answer;
    }
}