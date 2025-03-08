import java.io.*;
import java.util.*;

public class Main {
    static int M, N;
    static int[][] matrix;
    static int[] dx = { -1, 1, 0, 0 };
    static int[] dy = { 0, 0, -1, 1 };

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        M = Integer.parseInt(st.nextToken());
        N = Integer.parseInt(st.nextToken());

        matrix = new int[N][M];

        Queue<int[]> queue = new LinkedList<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                matrix[i][j] = Integer.parseInt(st.nextToken());
                if (matrix[i][j] == 1) {
                    queue.offer(new int[] { i, j });
                }
            }
        }

        bfs(queue);

        int days = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (matrix[i][j] == 0) {
                    System.out.println(-1);
                    return;
                }
                days = Math.max(days, matrix[i][j]);
            }
        }

        System.out.println(days - 1);
    }

    static void bfs(Queue<int[]> queue) {
        while (!queue.isEmpty()) {
            int[] pos = queue.poll();
            int x = pos[0], y = pos[1];

            for (int i = 0; i < 4; i++) {
                int nx = dx[i] + x, ny = dy[i] + y;

                if (nx >= 0 && nx < N && ny >= 0 && ny < M && matrix[nx][ny] == 0) {
                    matrix[nx][ny] = matrix[x][y] + 1;
                    queue.offer(new int[] { nx, ny });
                }
            }
        }
    }
}