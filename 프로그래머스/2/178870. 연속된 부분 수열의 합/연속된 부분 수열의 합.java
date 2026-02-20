class Solution {
    public int[] solution(int[] sequence, int k) {
        int[] answer = new int[]{0, sequence.length-1}; // 초기값은 기존 수열의 시작과 끝
        
        int start = 0, end = 0;
        
        int curr = sequence[0]; // 현재 부분 수열의 합
        
        while (start <= end) {
            if (curr == k) {
                if (end - start < answer[1] - answer[0]) { // 수열의 길이가 더 짧다면 업데이트
                    answer[0] = start;
                    answer[1] = end;
                }
                curr -= sequence[start];
                start += 1;
            } else if (curr < k) {
                end += 1;
                if (end == sequence.length) break;
                curr += sequence[end];
            } else if (curr > k) {
                curr -= sequence[start];
                start += 1;
            }
        }
        return answer;
    }
}