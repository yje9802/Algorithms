class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[num_list.length + 1];
        int size = num_list.length;
        if (num_list[size - 1] > num_list[size - 2]) {
            System.arraycopy(num_list, 0, answer, 0, size);
            answer[size] = num_list[size - 1] - num_list[size - 2];
        } else {
            System.arraycopy(num_list, 0, answer, 0, size);
            answer[size] = num_list[size - 1] * 2;
        }
        
        return answer;
    }
}