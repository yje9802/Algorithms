from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    
    def bfs(v):
        visited[v] = True # 방문처리
        
        dq = deque()
        dq.append(v)
        
        while dq:
            curr = dq.popleft()
            
            for i in range(n):
                if visited[i] == False and computers[curr][i] == 1:
                    visited[i] = True
                    dq.append(i)
    
    for v in range(n): # 시작지점이 정해져 있지 않아 모든 노드를 다 검사해야 함
        if not visited[v]:
            bfs(v)
            answer += 1
    
    return answer