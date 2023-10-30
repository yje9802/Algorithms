class Solution {
    public int solution(int order) {
        int answer = 0;
        String sorder = "" + order;
        String[] orders = sorder.split("");
        
        for (String o: orders) {
            if ("3".equals(o) || "6".equals(o) || "9".equals(o)) {
                answer++;
            }
        }
        
        return answer;
    }
}