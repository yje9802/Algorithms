import java.util.*;

class Solution {
    static int n, m;
    static int[][] directions = new int[][] { {-1, 0}, {1, 0}, {0, -1}, {0, 1} };
    
    public int solution(int[][] maze) {
        int answer = 0;
        
        n = maze.length;
        m = maze[0].length;
        
        int redX = 0, redY = 0;
        int blueX = 0, blueY = 0;
        int redGoalX = 0, redGoalY = 0;
        int blueGoalX = 0, blueGoalY = 0;
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (maze[i][j] == 1) {
                    redX = i;
                    redY = j;
                }
                if (maze[i][j] == 2) {
                    blueX = i;
                    blueY = j;
                }
                if (maze[i][j] == 3) {
                    redGoalX = i;
                    redGoalY = j;
                }
                if (maze[i][j] == 4) {
                    blueGoalX = i;
                    blueGoalY = j;
                }
            }
        }
        
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{ redX, redY, blueX, blueY, 1 << getIndex(redX, redY), 1 << getIndex(blueX, blueY), 0 });
        
        Set<String> visited = new HashSet<>();
        visited.add(redX + "," + redY + "," + blueX + "," + blueY + "," + (1 << getIndex(redX, redY)) + "," + (1 << getIndex(blueX, blueY)));
        
        while (!q.isEmpty()) {
            int[] temp = q.poll();
            int rx = temp[0], ry = temp[1], bx = temp[2], by = temp[3];
            int visitedRed = temp[4], visitedBlue = temp[5];
            int cnt = temp[6];
            
            if (rx == redGoalX && ry == redGoalY && bx == blueGoalX && by == blueGoalY) return cnt;
            
            int nrx, nry, nbx, nby;
            for (int[] dr: directions) {
                for (int[] db: directions) {
                    if (rx == redGoalX && ry == redGoalY) {
                        nrx = rx;
                        nry = ry;
                    } else {
                        nrx = rx + dr[0];
                        nry = ry + dr[1];
                    }
                    
                    if (bx == blueGoalX && by == blueGoalY) {
                        nbx = bx;
                        nby = by;
                    } else {
                        nbx = bx + db[0];
                        nby = by + db[1];
                    }
                    
                    if (!(0 <= nrx && nrx < n && 0 <= nry && nry < m) || (maze[nrx][nry] == 5)) {
                        nrx = rx;
                        nry = ry;
                    }
                    if (!(0 <= nbx && nbx < n && 0 <= nby && nby < m) || (maze[nbx][nby] == 5)) {
                        nbx = bx;
                        nby = by;
                    }
                    
                    // 서로 자리 바꾸기 X
                    if (nrx == bx && nry == by && nbx == rx && nby == ry) continue;
                    // 자리 겹치기 X
                    if (nrx == nbx && nry == nby) continue;
                    
                    // 이미 방문한 칸 재방문 X
                    if (!(rx==redGoalX && ry==redGoalY) && ((visitedRed & (1 << getIndex(nrx, nry))) != 0)) continue;
                    if (!(bx==blueGoalX && by==blueGoalY) && ((visitedBlue & (1 << getIndex(nbx, nby))) != 0)) continue;
                    
                    int newVisitedRed = visitedRed | (1 << getIndex(nrx, nry));
                    int newVisitedBlue = visitedBlue | (1 << getIndex(nbx, nby));
                    
                    String state = nrx + "," + nry + "," + nbx + "," + nby + "," + newVisitedRed + "," + newVisitedBlue;

                    if (visited.contains(state)) continue;
                    visited.add(state);
                    
                    q.add(new int[]{ nrx, nry, nbx, nby, newVisitedRed, newVisitedBlue, cnt+1 });
                }
            }
        }
        
        return answer;
    }
    
    public int getIndex(int x, int y) {
        return x * m + y;
    }
}