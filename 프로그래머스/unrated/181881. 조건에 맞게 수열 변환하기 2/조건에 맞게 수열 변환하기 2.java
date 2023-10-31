class Solution {
    public int solution(int[] arr) {
        int answer = -1;
        
        int loops = 0;
        while (answer == -1) {
            int changes = 0;
            for (int i = 0; i < arr.length; i++) {
                if (arr[i]%2 == 0 && arr[i] >= 50) {
                    arr[i] /= 2;
                    changes++;
                } else if (arr[i]%2 == 1 && arr[i] < 50) {
                    arr[i] = arr[i] * 2 + 1;
                    changes++;
                }
            }
            loops++;
            if (changes == 0) {
                answer = loops;
            }
        }
        
        return answer-1;
    }
}