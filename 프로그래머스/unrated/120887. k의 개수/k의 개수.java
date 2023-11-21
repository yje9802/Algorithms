class Solution {
    public int solution(int i, int j, int k) {
        int answer = 0;
        String sk = "" + k;
        for (int x = i; x <= j; x++) {
            String y = "" + x;
            if (y.contains(sk)) {
                for (int z = 0; z < y.length(); z++) {
                    if (y.charAt(z)==sk.charAt(0)) {
                        answer++;
                    }
                }
            }
        }
        return answer;
    }
}