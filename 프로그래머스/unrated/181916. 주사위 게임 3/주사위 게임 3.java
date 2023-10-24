import java.util.*;

class Solution {
    public int solution(int a, int b, int c, int d) {
        int answer = 0;
        int[] list = {a, b, c, d};
        Arrays.sort(list);
        
        if (list[0] == list[3]) {
            answer = 1111 * list[0];
        } else {
            if (list[1] == list[2]) {
                if (list[1] == list[0]) {
                    answer = (int) Math.pow((10*list[0]+list[3]), 2);
                } else if (list[1] == list[3]) {
                    answer = (int) Math.pow((10*list[3]+list[0]), 2);
                } else if (list[1] != list[0] && list[2] != list[3]) {
                    answer = list[0] * list[3];
                }
            } else {
                if (list[0] == list[1] && list[2] == list[3]) {
                    answer = (list[0] + list[3]) * Math.abs(list[0] - list[3]);
                } else if (list[0] == list[1] && list[2] != list[3]) {
                    answer = list[2] * list[3];
                } else if (list[0] != list[1] && list[2] == list[3]) {
                    answer = list[0] * list[1];
                } else if (list[0] != list[1] && list[2] != list[3]) {
                    answer = list[0];
                }
            }
        }
        
        return answer;
    }
}