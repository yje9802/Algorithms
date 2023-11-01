class Solution {
    public String[] solution(String[] quiz) {
        String[] answer = new String[quiz.length];
        
        for (int i = 0; i < quiz.length; i++) {
            String q = quiz[i];
            String[] math = q.split("=");
            String[] op = math[0].split(" ");
            
            int result = 0;
            int right = Integer.parseInt(math[1].trim());
            
            if (op[1].equals("+")) {
                result = Integer.parseInt(op[0]) + Integer.parseInt(op[2]);
            } else {
                result = Integer.parseInt(op[0]) - Integer.parseInt(op[2]);
            }
            
            if (result == right) {
                answer[i] = "O";
            } else {
                answer[i] = "X";
            }
        }
        return answer;
    }
}