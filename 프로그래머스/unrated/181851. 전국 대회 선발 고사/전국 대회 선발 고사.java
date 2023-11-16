import java.util.ArrayList;

class Solution {
    public int solution(int[] rank, boolean[] attendance) {
        int answer = 0;
        ArrayList<Integer> attends = new ArrayList<>();
        for (int i = 0; i< rank.length; i++) {
            if (attendance[i] == true) {
                attends.add(i);
            }
            if (attends.size() == 3) {
                break;
            }
        }
        
        for (int i = attends.get(0); i < rank.length; i++) {
            if (attendance[i] == true) {
                for (int j = 0; j < 3; j++) {
                    if (rank[i] == rank[attends.get(j)]) {
                        break;
                    }
                    if (rank[i] < rank[attends.get(j)]) {
                        attends.add(j, i);
                        attends.remove(3);
                        break;
                    } 
                }
            }
        }
        answer = 10000 * attends.get(0) + 100 * attends.get(1) + attends.get(2);
        return answer;
    }
}