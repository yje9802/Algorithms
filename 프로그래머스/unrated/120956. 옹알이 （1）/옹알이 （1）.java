class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        String[] possible = {"aya", "ye", "woo", "ma"};
        
        for (String s: babbling) {
            for (String p: possible) {
                s = s.replaceFirst(p, "_");
            }
            if (s.replaceAll("_", "").equals("")) {
                answer++;
            }
        }
        
        return answer;
    }
}