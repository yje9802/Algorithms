class Solution {
    public int solution(int n) {
        int answer = 0;
        int i = 1;
        int fact = 1;
        while (true) {
            if (fact > n) {
                i--;
                break;
            }
            i++;
            fact *= i;
        }
        answer = i;
        return answer;
    }
}