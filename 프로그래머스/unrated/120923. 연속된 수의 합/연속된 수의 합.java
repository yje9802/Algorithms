class Solution {
    public int[] solution(int num, int total) {
        int[] answer = new int[num];
        // total을 num으로 나눴을 때 몫이 보통 가운데 정도에 위치
        // 그럼 첫번째 숫자는
        int first = (total / num) - ((num - 1) / 2);
        for (int i = 0; i < num; i++) {
            answer[i] = first + i;
        }
        return answer;
    }
}