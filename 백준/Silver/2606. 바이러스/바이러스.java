import java.io.*;
import java.util.*;

public class Main {
    static List<Integer>[] graph; // 그래프 저장용 리스트 배열
    static boolean[] visited; // 방문 여부 체크
    static int count = 0; // 감염된 컴퓨터 수

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken()); // 컴퓨터 수

        st = new StringTokenizer(br.readLine());
        int M = Integer.parseInt(st.nextToken()); // 연결된 쌍 개수

        graph = new ArrayList[N + 1];

        visited = new boolean[N + 1];

        // 그래프 초기화
        for (int i = 1; i <= N; i++) {
            graph[i] = new ArrayList<>();
        }

        // 간선 정보 입력
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            graph[u].add(v);
            graph[v].add(u);
        }

        // DFS 탐색 시작 (1번 컴퓨터부터)
        dfs(1);

        // 1번 컴퓨터 제외하고 출력
        System.out.println(count - 1);
    }

    static void dfs(int node) {
        visited[node] = true;
        count++; // 방문한 노드 개수 증가

        for (int next : graph[node]) {
            if (!visited[next]) {
                dfs(next);
            }
        }
    }
}