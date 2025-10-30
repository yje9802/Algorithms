from collections import deque

def solution(maps):
    answer = 0
    
    n = len(maps)
    m = len(maps[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def bfs(start_x, start_y, end_x, end_y):
        dq = deque()
        visited = [[False] * m for _ in range(n)]
        
        visited[start_x][start_y] = True
        dq.append((start_x, start_y, 0))
        
        while dq:
            x, y, cost = dq.popleft()
            if x == end_x and y == end_y:
                return cost
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != 'X':
                    visited[nx][ny] = True
                    dq.append((nx, ny, cost+1))
        return -1
    
    S = L = E = None
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                S = (i, j)
            elif maps[i][j] == "L":
                L = (i, j)
            elif maps[i][j] == "E":
                E = (i, j)
        if S and L and E:
            break
    
    start_to_lever = bfs(S[0], S[1], L[0], L[1])
    lever_to_end = bfs(L[0], L[1], E[0], E[1])
    
    if start_to_lever == -1 or lever_to_end == -1:
        answer = -1
    else:
        answer = start_to_lever + lever_to_end
    
    return answer