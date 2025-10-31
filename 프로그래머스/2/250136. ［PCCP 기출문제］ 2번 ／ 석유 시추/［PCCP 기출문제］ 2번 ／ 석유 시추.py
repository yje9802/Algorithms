from collections import deque

def solution(land):
    answer = 0
    
    n = len(land) # 세로 길이
    m = len(land[0]) # 가로 길이
    
    position = [0] * m # position[i]는 i 열에서 뽑을 수 있는 석유 양
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * m for _ in range(n)]
    
    def bfs(start):
        dq = deque([(start[0], start[1])])
        
        visited[start[0]][start[1]] = True
        total_oil = 0
        columns = set()
        
        while dq:
            x, y = dq.popleft()
            total_oil += 1
            columns.add(y)
            
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and land[nx][ny] == 1:
                    visited[nx][ny] = True
                    dq.append((nx, ny))
        return (total_oil, columns)
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                total_oil, columns = bfs((i, j))
                for c in columns:
                    position[c] += total_oil
    
    answer = max(position)
    return answer