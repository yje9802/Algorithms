class Solution {
    public int solution(String binomial) {
        int answer = 0;
        String[] exs = binomial.split(" ");
        if (exs[1].equals("+")) {
            answer = Integer.parseInt(exs[0]) + Integer.parseInt(exs[2]);
        } else if (exs[1].equals("-")) {
            answer = Integer.parseInt(exs[0]) - Integer.parseInt(exs[2]);
        } else if (exs[1].equals("*")) {
            answer = Integer.parseInt(exs[0]) * Integer.parseInt(exs[2]);
        }
        return answer;
    }
}