import java.util.Arrays;

class Solution {
    public int solution(int[] array) {
        int answer = 0;
        Arrays.sort(array);
        int max = array[array.length - 1];
        
        int[] check = new int[max+1];
        for (int i = 0; i < array.length; i++) {
            check[array[i]]++;
        }
        int temp = Integer.MIN_VALUE;
        for (int i = 0; i < check.length; i++) {
            if (check[i] > temp) {
                temp = check[i];
                answer = i;
            } else if (check[i] == temp) {
                answer = -1;
            }
        } 
        return answer;
    }
}