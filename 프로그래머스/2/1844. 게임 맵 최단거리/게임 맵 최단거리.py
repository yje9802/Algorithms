from collections import deque

def solution(maps):
    answer = -1
    
    n = len(maps)
    m = len(maps[0])
    visited = [[False] * m for _ in range(n)] # 맵 방문 여부
    visited[0][0] = True # 출발 지점
    
    dq = deque([(0, 0, 1)]) # (x, y, 현재 거리)
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우
    
    while dq:
        x, y, dist = dq.popleft()
        
        # 목적지 도달
        if x == n-1 and y == m-1:
            return dist
        
        for i in range(4):
            nx, ny = x + directions[i][0], y + directions[i][1]
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    dq.append((nx, ny, dist+1))
    
    return answer