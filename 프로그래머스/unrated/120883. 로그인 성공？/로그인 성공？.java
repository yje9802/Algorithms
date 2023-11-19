class Solution {
    public String solution(String[] id_pw, String[][] db) {
        String answer = "fail";
        
        for (String[] db1: db) {
            if (id_pw[0].equals(db1[0])) {
                if (id_pw[1].equals(db1[1])) {
                    answer = "login";
                } else {
                    answer = "wrong pw";
                }
                break;
            } 
        }
        return answer;
    }
}