from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    
    MAX = 102 # 좌표의 최대가 50
    board = [[0] * MAX for _ in range(MAX)]
    
    # 1. 사각형 영역 1로 채우기 (2배 확대)
    for rec in rectangle:
        x1, y1, x2, y2 = [r*2 for r in rec]
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                board[x][y] = 1
    
    # 2. 테두리만 1로 남기기
    for rec in rectangle:
        x1, y1, x2, y2 = [r*2 for r in rec]
        for x in range(x1+1, x2):
            for y in range(y1+1, y2):
                board[x][y] = 0
    
    # 3. BFS로 최단 경로 찾기
    visited = [[0] * MAX for _ in range(MAX)]
    q = deque()
    q.append((characterX*2, characterY*2)) # 캐릭터 시작 위치
    visited[characterX*2][characterY*2] = 1
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    while q:
        x, y = q.popleft()
        if x == itemX*2 and y == itemY*2: # 목적지 도달
            return (visited[x][y]-1) // 2 # 2배 했던 걸 원래대로 되돌림
    
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if board[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    
    return answer