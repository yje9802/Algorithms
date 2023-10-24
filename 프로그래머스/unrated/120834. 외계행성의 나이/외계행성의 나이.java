class Solution {
    public String solution(int age) {
        String answer;
        String ages = ""+age;
        char[] sb = new char[ages.length()];
//         String[] arr = ages.split("");

//         for (int i = 0; i < arr.length; i++) {
//             answer += ((char) ( (Integer.parseInt(arr[i]) + 97))) ;
//         }
        for (int i = ages.length()-1; i >= 0; i--) {
            sb[i] = (char) ((age % 10) + (int)'a');
            age /= 10;
        } 
        answer = new String(sb);
        return answer;
    }
}