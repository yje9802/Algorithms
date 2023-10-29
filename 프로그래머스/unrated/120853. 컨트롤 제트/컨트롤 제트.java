class Solution {
    public int solution(String s) {
        int answer = 0;
        String[] ss = s.split(" ");
        
        for (int i = 0; i < ss.length; i++) {
            if ("Z".equals(ss[i])) {
                answer -= Integer.parseInt(ss[i-1]);
            } else {
                answer += Integer.parseInt(ss[i]);
            }
        }
        return answer;
    }
}