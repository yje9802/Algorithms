import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        Set<String> phoneSet = new HashSet<>();
        for (String number: phone_book) {
            phoneSet.add(number);
        }
        
        for (String number: phone_book) {
            StringBuilder temp = new StringBuilder();
            for (int i = 0; i < number.length()-1; i++) {
                temp.append(number.charAt(i));
                if (phoneSet.contains(temp.toString())) {
                    return false;
                }
            } 
        }
        
        return true;
    }
}