class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        myString = myString.replace("A", "C");
        myString = myString.replace("B", "D");
        myString = myString.replace("D", "A");
        myString = myString.replace("C", "B");
        
        if (myString.contains(pat)) {
            answer = 1;
        }
        return answer;
    }
}