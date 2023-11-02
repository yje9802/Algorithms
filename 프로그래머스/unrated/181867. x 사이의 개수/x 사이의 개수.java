class Solution {
    public int[] solution(String myString) {
        String[] to_sort = myString.split("x", myString.length());
        int[] answer = new int[to_sort.length];
        
        for (int i = 0; i < to_sort.length; i++) {
            answer[i] = to_sort[i].length();
        }
        return answer;
    }
}