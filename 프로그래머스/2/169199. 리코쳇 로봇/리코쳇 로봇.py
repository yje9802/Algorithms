from collections import deque

def solution(board):
    answer = 0
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    n, m = len(board), len(board[0])
    visited = [[False] * m for _ in range(n)]
    
    def bfs(x, y, cost):
        queue = deque()
        queue.append((x, y, cost))
        arrived = [] # G에 도달한 경우
        
        while queue:
            cx, cy, ccost = queue.popleft()
            for dx, dy in directions:
                nx, ny = cx, cy

                while True:
                    if 0 <= nx + dx < n and 0 <= ny + dy < m and board[nx + dx][ny + dy] != 'D':
                        nx, ny = nx + dx, ny + dy
                    else:
                        if visited[nx][ny]:
                            break
                        else:
                            if board[nx][ny] == 'G':
                                arrived.append(ccost + 1)
                            else:
                                visited[nx][ny] = True
                                queue.append((nx, ny, ccost + 1))
                            break
        return arrived
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                visited[i][j] = True
                result = bfs(i, j, 0)
                if len(result) == 0:
                    return -1
                else:
                    return min(result)
    return answer