from collections import deque

def solution(maze):
    answer = 0
    
    n, m = len(maze), len(maze[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def idx(x, y):
        return x * m + y
    
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1: red = (i, j) # 빨간 수레 시작 칸
            if maze[i][j] == 2: blue = (i, j) # 파란 수레 시작 칸
            if maze[i][j] == 3: red_goal = (i, j) # 빨간 수레 도착 칸
            if maze[i][j] == 4: blue_goal = (i, j) # 파란 수레 도착 칸
    
    start = (*red, *blue, 1 << idx(*red), 1 << idx(*blue), 0)
    visited = set([start[:-1]])  # (rx, ry, bx, by, maskR, maskB)
    dq = deque([start])
    
    while dq:
        rx, ry, bx, by, visited_red, visited_blue, cnt = dq.popleft()
        
        # 두 수레 모두 도착
        if (rx, ry) == red_goal and (bx, by) == blue_goal:
            return cnt
        
        # 두 수레는 매 턴 독립적으로 움직인다 -> 16가지 경우 가능
        for drx, dry in directions:
            for dbx, dby in directions:
                if (rx, ry) == red_goal:
                    nrx, nry = rx, ry
                else:
                    nrx, nry = rx + drx, ry + dry
                
                if (bx, by) == blue_goal:
                    nbx, nby = bx, by
                else:
                    nbx, nby = bx + dbx, by + dby

                # 가려는 방향이 벽이나거나 격자 밖이면 원래 자리에 머물기
                if not (0 <= nrx < n and 0 <= nry < m) or maze[nrx][nry] == 5:
                    nrx, nry = rx, ry
                if not (0 <= nbx < n and 0 <= nby < m) or maze[nbx][nby] == 5:
                    nbx, nby = bx, by

                # 겹침 금지
                if (nrx, nry) == (nbx, nby): continue
                # 수레끼리 자리 바꾸기 금지
                if (nrx, nry) == (bx, by) and (nbx, nby) == (rx, ry): continue

                # 방문했던 칸 재방문 금지, 이미 도착 칸에 위치한 경우 제외
                if (rx, ry) != red_goal and visited_red & (1 << idx(nrx, nry)): continue
                if (bx, by) != blue_goal and visited_blue & (1 << idx(nbx, nby)): continue

                # 새롭게 방문하는 칸 방문 처리
                new_visited_red = visited_red | (1 << idx(nrx, nry))
                new_visited_blue = visited_blue | (1 << idx(nbx, nby))

                curr = (nrx, nry, nbx, nby, new_visited_red, new_visited_blue)
                if curr in visited:
                    continue
                else:
                    visited.add(curr)
                dq.append((nrx, nry, nbx, nby, new_visited_red, new_visited_blue, cnt+1))
    
    return 0