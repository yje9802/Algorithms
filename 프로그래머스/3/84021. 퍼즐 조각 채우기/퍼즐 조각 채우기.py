from collections import deque

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우

def find_piece(board, xy, target): # bfs 사용
    # xy는 (x, y) 좌표 형태
    # target이 0이면 빈칸 모양을 찾는 거고, 1이면 퍼즐 조각 모양을 찾는 것
    n = len(board)
    dq = deque([xy])
    shape = []
    board[xy[0]][xy[1]] = -1 # 방문 표시
    
    while dq:
        x, y = dq.popleft()
        shape.append((x, y))
        
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == target:
                board[nx][ny] = -1
                dq.append((nx, ny))
    return normalize(shape)

def normalize(shape):
    # 찾은 모양을 (0,0) 기준으로 이동; 비교하기 위해
    min_x = min(x for x, y in shape)
    min_y = min(y for x, y in shape)
    
    normalized = sorted([(x-min_x, y-min_y) for x, y in shape])
    return normalized

def rotate(shape):
    # (x, y) -> 90도 회전하면 (y, -x)
    rotated = [(y, -x) for x, y in shape]
    return normalize(rotated)

def is_match(blank, puzzle):
    if len(blank) != len(puzzle):
        return False
    
    for _ in range(4):
        puzzle = rotate(puzzle)
        if puzzle == blank:
            return True
    return False

def solution(game_board, table):
    answer = 0
    
    n = len(game_board)
    
    blanks = []   
    # 빈칸 모양 찾기
    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0:
                blanks.append(find_piece(game_board, (i, j), 0))
    
    puzzles = []
    # 퍼즐 조각 모양 찾기
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1:
                puzzles.append(find_piece(table, (i, j), 1))
    
    used = [False] * len(puzzles)
    
    for blank in blanks:
        for i, puzzle in enumerate(puzzles):
            if used[i]: # 이미 사용된 퍼즐 조각이면 넘어감
                continue
            if is_match(blank, puzzle):
                answer += len(puzzle)
                used[i] = True
                break # 이 빈칸은 이제 채워졌으니 다른 빈칸으로 넘어감
            
    return answer