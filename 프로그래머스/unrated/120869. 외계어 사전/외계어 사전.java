class Solution {
    public int solution(String[] spell, String[] dic) {
        int answer = 0;
        for (String d: dic) {
            for (String s: spell) {
                if (d.contains(s)) {
                    answer++;
                }
            }
            if (answer == spell.length) {
                answer = 1;
                break;
            }
            answer = 0;
        }
        if (answer != 1) {
            answer = 2;
        }
        return answer;
    }
}