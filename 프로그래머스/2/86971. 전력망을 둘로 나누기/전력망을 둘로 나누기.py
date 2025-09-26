def solution(n, wires):
    answer = n
    
    def dfs(start, graph, visited, removed):
        visited[start] = True
        count = 1
        
        for node in graph[start]:
            if node == removed:
                continue
            if not visited[node]:
                count += dfs(node, graph, visited, removed)
        
        return count
    
    graph = [[] for _ in range(n+1)] # 연결된 노드 저장
    for u, v in wires:
        graph[u].append(v)
        graph[v].append(u)
    
    for u, v in wires:
        visited = [False] * (n+1)
        cnt = dfs(u, graph, visited, v)
        diff = abs(cnt - (n - cnt))
        answer = min(answer, diff)
    
    return answer