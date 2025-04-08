import java.io.*;
import java.util.*;

public class Main {
    static int answer = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int[] nums = new int[N];
        for (int i = 0; i < N; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(nums);

        for (int i = 0; i < N; i++) {
            int target = nums[i];
            int left = 0;
            int right = N - 1;

            while (left < right) {
                if (nums[left] + nums[right] == target) {
                    if (left != i && right != i) {
                        answer++;
                        break;
                    } else if (left == i) {
                        left++;
                    } else {
                        right--;
                    }
                } else if (nums[left] + nums[right] < target) {
                    left++;
                } else if (nums[left] + nums[right] > target) {
                    right--;
                }
            }
        }

        System.out.println(answer);
    }
}