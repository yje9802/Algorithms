import java.util.*;
import java.io.*;

class Main {
    static int N, M;
    static ArrayList<Integer>[] subjects; // i번 과목을 수강한 후에 수강 가능한 과목 리스트
    static int[] nPre; // i번 과목을 듣기 위해 필요한 선수과목의 개수
    static int[] semesters; // i번 과목을 들을 수 있는 학기

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken()); // 과목 수
        M = Integer.parseInt(st.nextToken()); // 선수조건 수

        subjects = new ArrayList[N + 1];
        nPre = new int[N + 1];
        semesters = new int[N + 1];

        for (int i = 1; i < N + 1; i++) {
            subjects[i] = new ArrayList<>();
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());

            subjects[A].add(B);
            nPre[B]++;
        }

        topologicalSort();

        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= N; i++) {
            sb.append(semesters[i]).append(" ");
        }
        System.out.println(sb);
    }

    static void topologicalSort() {
        Queue<Integer> queue = new LinkedList<>();

        // 선수 과목이 없는 과목부터 시작
        for (int i = 1; i <= N; i++) {
            if (nPre[i] == 0) {
                queue.offer(i);
                semesters[i] = 1;
            }
        }

        while (!queue.isEmpty()) {
            int curr = queue.poll();

            for (int next : subjects[curr]) {
                nPre[next]--;
                semesters[next] = Math.max(semesters[next], semesters[curr] + 1);

                // 선수과목을 전부 들은 경우
                if (nPre[next] == 0) {
                    queue.offer(next);
                }
            }
        }
    }
}