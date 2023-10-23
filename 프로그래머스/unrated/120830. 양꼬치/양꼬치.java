class Solution {
    public int solution(int n, int k) {
        int answer = 0;
        int service = (int) n / 10;
        answer = n * 12000 + 2000 * (k - service);
        return answer;
    }
}