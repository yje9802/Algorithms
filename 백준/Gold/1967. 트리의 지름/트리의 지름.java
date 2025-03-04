import java.io.*;
import java.util.*;

public class Main {
    static List<Node>[] tree;
    static boolean[] visited;
    static int maxDist = 0;
    static int farthestNode = 0;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        if (n == 1) {
            System.out.println(0);
            return;
        }

        tree = new ArrayList[n + 1]; // 2차원 배열
        for (int i = 0; i <= n; i++) {
            tree[i] = new ArrayList<>();
        }

        for (int i = 0; i < n - 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());
            tree[a].add(new Node(b, cost));
            tree[b].add(new Node(a, cost));
        }

        // 1번 노드에서 가장 먼 노드 찾기
        visited = new boolean[n + 1];
        visited[1] = true;
        dfs(1, 0);

        // 찾은 노드에서 가장 먼 노드까지 거리 찾기
        visited = new boolean[n + 1];
        maxDist = 0; // 전역 변수이므로 다시 초기화
        visited[farthestNode] = true;
        dfs(farthestNode, 0);

        System.out.println(maxDist);
    }

    static void dfs(int node, int dist) {
        if (dist > maxDist) {
            maxDist = dist;
            farthestNode = node;
        }

        for (Node next : tree[node]) {
            if (!visited[next.to]) {
                visited[next.to] = true;
                dfs(next.to, dist + next.cost);
            }
        }
    }

    static class Node {
        int to, cost;

        Node(int to, int cost) {
            this.to = to;
            this.cost = cost;
        }
    }
}