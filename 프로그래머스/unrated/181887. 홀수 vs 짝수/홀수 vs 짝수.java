class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        int odds = 0;
        int evens = 0;
        
        for (int i = 0; i < num_list.length; i++) {
            if (i % 2 == 0) {
                odds += num_list[i];
            } else {
                evens += num_list[i];
            }
        }
        answer = Math.max(odds, evens);
        return answer;
    }
}