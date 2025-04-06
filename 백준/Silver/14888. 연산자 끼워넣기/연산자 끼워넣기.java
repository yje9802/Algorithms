import java.io.*;
import java.util.*;

public class Main {
    static int N;
    static int[] nums;
    static int[] ops = new int[4]; // + - * /
    static int maxResult = Integer.MIN_VALUE;;
    static int minResult = Integer.MAX_VALUE;;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        nums = new int[N];
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 4; i++) {
            ops[i] = Integer.parseInt(st.nextToken());
        }

        dfs(1, nums[0], ops[0], ops[1], ops[2], ops[3]);

        System.out.println(maxResult);
        System.out.println(minResult);
    }

    static void dfs(int cnt, int currResult, int plus, int minus, int multiply, int divide) {
        if (cnt == N) {
            maxResult = Math.max(maxResult, currResult);
            minResult = Math.min(minResult, currResult);
            return;
        }

        if (plus > 0) { // 더하기 연산자가 더 남아있다면
            dfs(cnt + 1, currResult + nums[cnt], plus - 1, minus, multiply, divide);
        }
        if (minus > 0) {
            dfs(cnt + 1, currResult - nums[cnt], plus, minus - 1, multiply, divide);
        }
        if (multiply > 0) {
            dfs(cnt + 1, currResult * nums[cnt], plus, minus, multiply - 1, divide);
        }
        if (divide > 0) {
            int temp;
            if (currResult < 0) {
                temp = -(-currResult / nums[cnt]);
            } else {
                temp = currResult / nums[cnt];
            }
            dfs(cnt + 1, temp, plus, minus, multiply, divide - 1);
        }
    }
}