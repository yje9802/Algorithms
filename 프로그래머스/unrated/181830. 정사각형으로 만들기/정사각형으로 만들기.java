class Solution {
    public int[][] solution(int[][] arr) {
        int len = arr.length > arr[0].length ? arr.length : arr[0].length;
        int[][] answer = new int[len][len];
        
        if (len == arr.length) {
            for (int i = 0; i < len; i++) {
                for (int j = 0; j < len; j++) {
                    if (j >= arr[0].length) {
                        answer[i][j] = 0;
                    } else {
                       answer[i][j] = arr[i][j]; 
                    }
                }
            }
        } else {
            for (int i = 0; i < len; i++) {
                for (int j = 0; j < len; j++) {
                    if (i >= arr.length) {
                        answer[i][j] = 0;
                    } else {
                        answer[i][j] = arr[i][j];
                    }
                }
            }
        }
        return answer;
    }
}