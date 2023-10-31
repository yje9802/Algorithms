class Solution {
    public int[] solution(int n) {
        int[] answer;
        String divine = "";
        for (int i = 1; i < n + 1; i++) {
            if (n % i == 0) {
                divine += i + ",";
            }
        }
        String[] divines = divine.split(",");
        answer = new int[divines.length];
        for (int j = 0; j < divines.length; j++) {
            answer[j] = Integer.parseInt(divines[j]);
        }
        return answer;
    }
}