class Solution {
    public String[] solution(String[] names) {
        String[] answer;
        String groups = "";
        
        for (int i = 0; i < names.length; i += 5) {
            groups += names[i] + ",";
        }
        answer = groups.split(",");
        return answer;
    }
}