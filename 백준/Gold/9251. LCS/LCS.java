import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String word1 = br.readLine().trim();
        String word2 = br.readLine().trim();
        
        int l1 = word1.length();
        int l2 = word2.length();
        int[] cache = new int[l2]; // word2에 대해 캐시 지정

        for (int i = 0; i < l1; i++) {
            int cnt = 0; // 누적값을 저장할 변수
            for (int j = 0; j < l2; j++) {
                if (cnt < cache[j]) { // cnt를 최신 상태(최댓값)로 유지
                    cnt = cache[j];
                } else if (word1.charAt(i) == word2.charAt(j)) {
                    cache[j] = cnt + 1;
                }
            }
        }

        int maxLCS = 0;
        for (int val : cache) {
            maxLCS = Math.max(maxLCS, val);
        }
        System.out.println(maxLCS);
    }
}