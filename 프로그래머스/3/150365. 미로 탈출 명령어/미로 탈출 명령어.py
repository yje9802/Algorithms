from collections import deque

def solution(n, m, x, y, r, c, k):
    answer = ''
    
    start = (x-1, y-1)
    end = (r-1, c-1)
    
    def reachable(cx, cy, cost):
        manhattan = abs(cx - end[0]) + abs(cy - end[1])
        if manhattan <= cost and (cost - manhattan) % 2 == 0:
            return True
        return False
    
    if not reachable(*start, k): # 애초에 도달 불가능
        return "impossible"
    
    directions = [(1, 0, "d"), (0, -1, "l"), (0, 1, "r"), (-1, 0, "u")]
    dq = deque([("", *start, k)])
    while dq:
        route, cx, cy, cnt = dq.popleft()
        
        if cnt == 0:
            if (cx, cy) == end:
                return route
            continue
        
        for dx, dy, dr in directions:
            nx, ny, nroute = cx + dx, cy + dy, route + dr
            if 0 <= nx < n and 0 <= ny < m:
                if reachable(nx, ny, cnt-1):
                    dq.append((nroute, nx, ny, cnt - 1))
                    break
        
    return "impossible"