class Solution {
    public int solution(String my_string) {
        int answer = 0;
        String[] ss = my_string.split(" ");
        int i = 0;
        while (i < ss.length) {
            if ("+".equals(ss[i])) {
                answer += Integer.parseInt(ss[i+1]);
                i = i + 2;
            } else if ("-".equals(ss[i])) {
                answer -= Integer.parseInt(ss[i+1]);
                i = i + 2;
            } else {
                answer += Integer.parseInt(ss[i]);
                i++;
            }
        }
        return answer;
    }
}