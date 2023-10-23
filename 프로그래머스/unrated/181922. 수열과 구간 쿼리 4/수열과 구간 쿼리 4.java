class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        // int[] answer = new int[arr.length];
        for (int[] q: queries) {
            for (int i = q[0]; i <= q[1]; i++) {
                if (i % q[2] == 0) {
                    arr[i] = arr[i] + 1;
                }
            }
        }
        return arr;
    }
}