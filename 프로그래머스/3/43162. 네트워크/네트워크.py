def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    
    def dfs(v):
        visited[v] = True # 방문처리
        
        for node_n in range(n):
            # 아직 방문하지 않은 노드면서 v 노드와 연결되어 있을 때
            if not visited[node_n] and computers[v][node_n] == 1:
                dfs(node_n)
    
    for v in range(n): # 시작지점이 정해져 있지 않아 모든 노드를 다 검사해야 함
        if not visited[v]:
            dfs(v)
            answer += 1
    
    return answer