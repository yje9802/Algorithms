from collections import deque

def solution(maps):
    answer = []
    
    n, m = len(maps), len(maps[0]) # n은 세로 길이, m은 가로 길이
    visited = [[False] * m for _ in range(n)]
    
    def bfs(x, y):
        cost = int(maps[x][y])
        dq = deque([(x, y)]) # 시작점부터
        visited[x][y] = True
        
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while dq:
            cx, cy = dq.popleft()
            for dx, dy in dirs:
                nx, ny = cx + dx, cy + dy
                if (0 <= nx < n and 0 <= ny < m) and not visited[nx][ny] and maps[nx][ny] != 'X':
                    dq.append((nx, ny))
                    visited[nx][ny] = True
                    cost += int(maps[nx][ny])
        return cost
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                answer.append(bfs(i, j))
            
    return sorted(answer) if answer else [-1]